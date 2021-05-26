import pyrosetta
from pyrosetta import rosetta
import matching_binding_sites.scripts.fast_match as fm

def main():
    pyrosetta.init()
    print('starting')

    site_pose = pyrosetta.pose_from_file('./test_inputs/5kp4B_3respkt.pdb')
    scaffold_pose = pyrosetta.pose_from_file('./test_inputs/clean_5kp4A.pdb')
    # scaffold_pose = pyrosetta.pose_from_file('./test_inputs/3fh1A00.pdb')

    site_protein_residues = [i for i in range(1, site_pose.size() + 1) if site_pose.residue(i).is_protein()] 
    scaffold_protein_residues = [i for i in range(1, scaffold_pose.size() + 1) if scaffold_pose.residue(i).is_protein()]
    print('ok')
    print(fm.fast_match(site_pose, site_protein_residues, scaffold_pose, scaffold_protein_residues, 'test_output',
        cut_off_max_dist=2, cut_off_max_rmsd=1, cut_off_min_direction_cos=0.7, dump_matches=True, dump_trajectory=True))
    # print(fm.fast_match(site_pose, site_protein_residues, scaffold_pose, scaffold_protein_residues, 'test_output',
    #     cut_off_max_dist=5, cut_off_max_rmsd=5, cut_off_min_direction_cos=1, dump_matches=False, dump_trajectory=False))

if __name__ == '__main__':
    main()
