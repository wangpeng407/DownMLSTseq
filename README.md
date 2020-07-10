### script for downloading MLST sequences

### Usage:

```
Download housekeeping gene sequences from https://pubmlst.org/data/dbases.xml

optional arguments:
  -h, --help            show this help message and exit
  -s SPECIES, --species SPECIES
                        species name
  -f, --writefile       write out all available species gene file
  -a, --available       print all available species for MLST
  -m DOWN_MODE, --down_mode DOWN_MODE
                        type of download, 1, wget , 2 request
  -o OUTPUT, --output OUTPUT
                        output directory, default is ./

```

#### Example 1: print available species for MLST
```
python parse_xml_down_mlst.data.py -a -o out


####################################################################################################
All available species are as follows, choose one from them:
Achromobacter spp. | Acinetobacter baumannii#1 | Acinetobacter baumannii#2 | Aeromonas spp. | Anaplasma phagocytophilum | Arcobacter spp. | Aspergillus fumigatus | Bacillus cereus | Bacillus licheniformis | Bacillus subtilis | Bartonella bacilliformis | Bartonella henselae | Bartonella washoensis | Bordetella spp. | Borrelia spp. | Brachyspira hampsonii | Brachyspira hyodysenteriae | Brachyspira intermedia | Brachyspira pilosicoli | Brachyspira spp. | Brucella spp. | Burkholderia cepacia complex | Burkholderia pseudomallei | Campylobacter concisus/curvus | Campylobacter fetus | Campylobacter helveticus | Campylobacter hyointestinalis | Campylobacter insulaenigrae | Campylobacter jejuni | Campylobacter lanienae | Campylobacter lari | Campylobacter sputorum | Campylobacter upsaliensis | Candida albicans | Candida glabrata | Candida krusei | Candida tropicalis | Candidatus Liberibacter solanacearum | Carnobacterium maltaromaticum | Chlamydiales spp. | Citrobacter freundii | Clonorchis sinensis | Clostridioides difficile | Clostridium botulinum | Clostridium septicum | Corynebacterium diphtheriae | Cronobacter spp. | Dichelobacter nodosus | Edwardsiella spp. | Enterobacter cloacae | Enterococcus faecalis | Enterococcus faecium | Escherichia coli#1 | Escherichia coli#2 | Flavobacterium psychrophilum | Gallibacterium anatis | Haemophilus influenzae | Haemophilus parasuis | Helicobacter cinaedi | Helicobacter pylori | Helicobacter suis | Kingella kingae | Klebsiella aerogenes | Klebsiella oxytoca | Klebsiella pneumoniae | Kudoa septempunctata | Lactobacillus salivarius | Leptospira spp. | Leptospira spp.#2 | Leptospira spp.#3 | Listeria monocytogenes | Macrococcus canis | Macrococcus caseolyticus | Mannheimia haemolytica | Melissococcus plutonius | Moraxella catarrhalis | Mycobacteria spp. | Mycobacterium abscessus | Mycobacterium massiliense | Mycoplasma agalactiae | Mycoplasma bovis | Mycoplasma flocculare | Mycoplasma gallisepticum#1 | Mycoplasma gallisepticum#2 | Mycoplasma hominis | Mycoplasma hyopneumoniae | Mycoplasma hyorhinis | Mycoplasma iowae | Mycoplasma pneumoniae | Mycoplasma synoviae | Neisseria spp. | Orientia tsutsugamushi | Ornithobacterium rhinotracheale | Paenibacillus larvae | Pasteurella multocida#1 | Pasteurella multocida#2 | Pediococcus pentosaceus | Photobacterium damselae | Piscirickettsia salmonis | Porphyromonas gingivalis | Propionibacterium acnes | Pseudomonas aeruginosa | Pseudomonas fluorescens | Pseudomonas putida | Rhodococcus spp. | Riemerella anatipestifer | Salmonella enterica | Saprolegnia parasitica | Sinorhizobium spp. | Staphylococcus aureus | Staphylococcus epidermidis | Staphylococcus haemolyticus | Staphylococcus hominis | Staphylococcus lugdunensis | Staphylococcus pseudintermedius | Stenotrophomonas maltophilia | Streptococcus agalactiae | Streptococcus bovis/equinus complex (SBSEC) | Streptococcus canis | Streptococcus dysgalactiae equisimilis | Streptococcus gallolyticus | Streptococcus oralis | Streptococcus pneumoniae | Streptococcus pyogenes | Streptococcus suis | Streptococcus thermophilus | Streptococcus thermophilus#2 | Streptococcus uberis | Streptococcus zooepidemicus | Streptomyces spp | Taylorella spp. | Tenacibaculum spp. | Treponema pallidum | Trichomonas vaginalis | Ureaplasma spp. | Vibrio cholerae | Vibrio cholerae#2 | Vibrio parahaemolyticus | Vibrio spp. | Vibrio tapetis | Vibrio vulnificus | Wolbachia | Xylella fastidiosa | Yersinia pseudotuberculosis | Yersinia ruckeri | Yersinia spp.

```

#### Example 2: download mlst files of "Achromobacter spp."

```
python parse_xml_down_mlst.data.py -m 2 -o out  -f  -s 'Achromobacter spp.'
```



