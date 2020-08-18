from Bio.PDB import *
import os, shutil
#set preparation pathways
prepare_protein_path = '~/MGLTools-1.5.6/bin/pythonsh ~/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -A bonds_hydrogens -U nphs_lps_waters_nonstdres -r'
prepare_ligand_path = '~/MGLTools-1.5.6/bin/pythonsh ~/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -A bonds_hydrogens -U nphs_lps -l'

"""Class inheriting from Select checking if the residue is aminoacid"""
class ResSelect(Select):
    def accept_residue(self, residue):
        if is_aa(residue):
            return 1
        else:
            return 0


class ProteinPreparer:

    def __init__(self, protein: str):
        self.protein = protein
        self.filename = './raw_ents/pdb{}.ent'.format(self.protein)

    def prepare_protein(self):
        parser = PDBParser()
        io = PDBIO()
        PDBList().retrieve_pdb_file(pdb_code=self.protein, pdir='./raw_ents/', file_format='pdb')
        ipdb = parser.get_structure('ipdb', self.filename)  # Input pdb as a self.file
        io.set_structure(ipdb)  # Setting structure for input pdb
        # shutil.move(self.protein,
        #             '/home/rmadeye/PycharmProjects/residue_modifier/databases/pdb_raw/')  # Moving old structure to raw pdb databasde
        io.save('./prepared_protein_pdbs/'+self.protein+'.pdb', ResSelect(), preserve_atom_numbering=True)
        os.system(prepare_protein_path + './prepared_protein_pdbs/{}.pdb'.format(self.protein))
        shutil.move(self.protein+'.pdbqt','./protein_pdbqts/')
