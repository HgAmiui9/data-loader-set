import os
import SimpleITK as sitk

def getSubjectList():

    subjects_path = os.path.join(os.path.abspath(os.getcwd()), 'data/subjects.txt')
    file = open(subjects_path, "r", encoding = 'utf-8')
    subjects_list = file.readlines()
    subjects_list = [x.rstrip('\n') for x in subjects_list]
    return subjects_list

def getSubjectData(subjectID):

    img_path = os.path.join(os.path.abspath(os.getcwd()), 'data/' + subjectID + '/aligned_norm.nii.gz')
    img = sitk.ReadImage(img_path)
    print(img)

    return img

if __name__ == "__main__":
    list = getSubjectList()
    print(getSubjectData(list[0]))
