import pydicom
import matplotlib.pyplot as plt
import pathlib
import os

paths = pathlib.Path('CBCT to sCT')
all_CT_paths = list(paths.glob('*'))
all_CT_paths = [str(path) for path in all_CT_paths]
sub_paths = {0}

for i in (all_CT_paths):
    dir_1 = i.replace('CBCT to sCT', 'CBCT和CT图的二维图像')
    if(not(os.path.exists(dir_1))):
        os.makedirs(dir_1)
    s_paths = pathlib.Path(i)
    s_paths = list(s_paths.glob('*'))
    s_paths = [str(p) for p in s_paths]
    for j in s_paths:
        dir_2 = j.replace('CBCT to sCT', 'CBCT和CT图的二维图像')
        if(not(os.path.exists(dir_2))):
            os.makedirs(dir_2)
        c_paths = pathlib.Path(j)
        c_paths = list(c_paths.glob('*'))
        c_paths = [str(p) for p in c_paths]
        for CT in c_paths:
            print(CT)
            try:
                dcm = pydicom.read_file(CT, force=True)
                dcm.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
                dir_name = CT.replace('CBCT to sCT','CBCT和CT图的二维图像')
                dir_name += ".png"
                plt.figure()
                plt.imshow(dcm.pixel_array, cmap='gray')
                plt.xticks([])
                plt.yticks([])
            except  AttributeError:
                continue
            else:
                if(not(os.path.exists(dir_name))):
                    plt.savefig(dir_name)
            

# plt.figure()
# for i in range(88):
#     if(i>=10):
#         dcm = pydicom.read_file(r'D:/CBCT to sCT/00c1240579/pCT/00C1240579_CT1_image000'+ str(i) +'.DCM',force=True)
#     else:
#         dcm = pydicom.read_file(r'D:/CBCT to sCT/00c1240579/pCT/00C1240579_CT1_image0000'+ str(i) +'.DCM',force=True)
#     dcm.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
#     plt.imshow(dcm.pixel_array,cmap='gray')
#     plt.show()

# plt.figure()
# dcm = pydicom.read_file(r'D:/CBCT to sCT/0000397791/day15/CT_1.3.46.423632.3358082018121771757843.68',force=True)
# dcm.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
# plt.imshow(dcm.pixel_array,cmap='gray')
# plt.show()
