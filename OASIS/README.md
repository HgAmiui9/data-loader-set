# OASIS-1
## Summary
This set consists of a cross-sectional collection of 416 subjects aged 18 to 96. For each subject, 3 or 4 individual T1-weighted MRI scans obtained in single scan sessions are included. The subjects are all right-handed and include both men and women. 100 of the included subjects over the age of 60 have been clinically diagnosed with very mild to moderate Alzheimer’s disease (AD). Additionally, a reliability data set is included containing 20 nondemented subjects imaged on a subsequent visit within 90 days of their initial session.

For analysis, AD patients were upsampled to balance the dataset.

## Download
[Download v1.0 here (6.6G)](https://surfer.nmr.mgh.harvard.edu/ftp/data/neurite/data/neurite-oasis.v1.0.tar)  
[Download v1.0 here 2D only (24M)](https://surfer.nmr.mgh.harvard.edu/ftp/data/neurite/data/neurite-oasis.2d.v1.0.tar)

## Analyse
### Data description
| S.NO. | Attributes | Description |
| --- | --- | --- |
| 1 | ID | Identification |
| 2 | M/F | Gender(Male or Female) |
| 3 | Hand | Handedness |
| 4 | Age | Age in years |
| 5 | EDUC | Years of education |
| 5 | SES | Socio Economic Status |
| 6 | MMSE | Mini Mental State Examination |
| 7 | CDR | Clinical Dementia Rating |
| 8 | eTIV | Estimated Total Intracranial Volume |
| 9 | nWBV | Normalize Whole Brain Volume |
| 10 | nWBV | Normalize Whole Brain Volume |
| 11 | ASF | Atlas Scaling Factor |
| 12 | Delay | Delay |

### CDR 
CDR means Clinical Dementia Rating, which is the label of AD.
>0   = absent
0.5 = questionable
1   = present, but mild
2   = moderate
3   = severe
4   = profound
5   = terminal

0 -> 0, false; [0.5,1]->1, true
| Label | Number |
| --- | --- |
| NAD | 135 |
| AD | 98 (70,28)|
| Unknow | 203 |
| Amount | 436 |

### Data divide
In supervised classification,  only select CDR not NaN data. Then devide then.
>training ---> 80%
test ---> 20%
