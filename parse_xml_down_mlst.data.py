#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os
import xml.etree.ElementTree as ET
from urllib.request import urlretrieve
import argparse

url = 'https://pubmlst.org/data/dbases.xml'

def parse_args():
    parser = argparse.ArgumentParser(description="Download housekeeping gene sequences from " + url)
    parser.add_argument("-s", "--species", type = str,help="species name")
    parser.add_argument("-f", "--writefile", action="store_true", help="write out all available species gene file")
    parser.add_argument('-a', "--available", action="store_true", help="print all available species for MLST")
    parser.add_argument('-m', '--down_mode', type = int, default=1, help="type of download, 1, wget , 2 request")
    parser.add_argument("-o", "--output", type = str, default='./', required=False,help="output directory, default is ./")
    args = parser.parse_args()
    return args

def retrieve(url, outfile):
    try:
        sys.stderr.write("\nDownloading " + url + "\n")
        file, headers = urlretrieve(url, outfile)
    except EnvironmentError:
        sys.stderr.write("\nWarning: Unable to download " + url + "\n")

def wget_file(url, outfile):
    try:
        sys.stderr.write("\nwget " + url + "\n")
        cmd = 'wget --tries=0 ' + url + ' -q -O ' + outfile
        os.system(cmd)
    except:
        sys.stderr.write("\nWarning: Unable to wget " + url + "\n")

def download_files(url, outfile, type = 1):
    if type == 1:
        wget_file(url, outfile)
    else:
       retrieve(url, outfile)

def parse_xml(in_xml):
    root = ET.parse(in_xml).getroot()
    species_profiles_gene = {}
    for sp in root.iter('species'):
        species = str(sp.text).rstrip()
        species_profiles_gene[species] = {}
        for mlst in sp.iter('mlst'):
            for database in mlst:
                for profiles in database.iter('profiles'):
                    species_profiles_gene[species]['profiles'] = str(profiles.find('url').text)
                for loci in database.iter('loci'):
                    for locus in loci.iter('locus'):
                        locus_str = str(locus.text).rstrip()
                        species_profiles_gene[species][locus_str] = str(locus.find('url').text)

    return species_profiles_gene

def main():
    args = parse_args()
    if not os.path.isdir(args.output):
        os.makedirs(args.output)
    outdir = os.path.abspath(args.output)
    xml_out = os.path.join(outdir, 'pubmlst_data.xml')
    list_out = os.path.join(outdir, 'pubmlst_data.list')
    if not os.path.isfile(xml_out):
        download_files(url = url, outfile=xml_out, type = args.down_mode)
    else:
        print(xml_out + " already present!")
    SpeProGene = parse_xml(xml_out)
    sort_spe = sorted(SpeProGene.keys())
    if args.available:
        print("\033[1;35;31m#"*100)
        print("All available species are as follows, choose one from them:\033[0m")
        print(" | ".join(sort_spe))
        exit()
    if args.species not in sort_spe:
        print("\033[1;35;31m#"*100)
        print("Warning: you can only choose one from them:\033[0m")
        print(" | ".join(sort_spe))
        exit()

    if args.writefile:
        fileout = open(list_out, 'w')
        fileout.write("species\tgene_name\taddr\n")
    for s,v1 in SpeProGene.items():
        for g,addr in v1.items():
            spe = s.replace(' ', '_')
            if g == 'profiles':
                temp_out = os.path.join(outdir, spe + '.' + g + '.txt')
            else:
                temp_out = os.path.join(outdir, spe + '.' + g + '.tfa')
            if os.path.isfile(temp_out):
                print(temp_out + " already present!")
                continue
            if s == args.species:
                download_files(addr, temp_out, type = args.down_mode)
            cont = s + "\t" + g + "\t" + addr + "\n"
            if args.writefile:
                fileout.write(cont)
    if args.writefile:
        fileout.close()

if __name__ == '__main__':
    main()

