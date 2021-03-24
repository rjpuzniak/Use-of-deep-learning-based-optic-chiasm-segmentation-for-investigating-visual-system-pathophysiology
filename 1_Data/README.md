# Data

This folder stores all the data linked to (Puzniak & Hoffmann, in preparation), which will be downloaded and generated through provided scripts ("2_Code" folder). Once complete, this folder will be organized as follows:

```bash
├── 1_T1w_Images_and_Labels
│   ├── 1_T1w_Images
│   │   ├── CHIASM [19 entries]
│   │   └── HCP [1066 entries]
│   ├── 2_Optic_Chiasm_Labels_Initial
│   │   ├── CHIASM [19 entries]
│   │   └── HCP [1112 entries]
│   ├── 3_Optic_Chiasm_Labels_Refined
│   │   ├── CHIASM [19 entries]
│   │   └── HCP [1065 entries]
│   ├── 4_Optic_Chiasm_Labels_Handmade_Original
│   │   ├── CHIASM [19 entries]
│   │   └── HCP [10 entries]
│   ├── 5_Optic_Chiasm_Labels_Handmade_Cropped_to_initial
│   │   ├── CHIASM [19 entries]
│   │   └── HCP [10 entries]
│   └── 6_Optic_Chiasm_Labels_Handmade_Cropped_to_refined
│       ├── CHIASM [19 entries]
│       └── HCP [10 entries]
├── 2_DCNN_Predictions
│   ├── training_100ep_00005lr_dice
│   │   ├── connectivity_1
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   ├── connectivity_2
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   └── connectivity_3
│   │       ├── threshold_0.25
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.5
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.75
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       └── threshold_1
│   │           ├── CHIASM [19 entries]
│   │           └── HCP [10 entries]
│   ├── training_13ep_00025lr_dice
│   │   ├── connectivity_1
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   ├── connectivity_2
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   └── connectivity_3
│   │       ├── threshold_0.25
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.5
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.75
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       └── threshold_1
│   │           ├── CHIASM [19 entries]
│   │           └── HCP [10 entries]
│   ├── training_15ep_0003lr_dice
│   │   ├── connectivity_1
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   ├── connectivity_2
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   └── connectivity_3
│   │       ├── threshold_0.25
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.5
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.75
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       └── threshold_1
│   │           ├── CHIASM [19 entries]
│   │           └── HCP [10 entries]
│   ├── training_30ep_00025lr_dice
│   │   ├── connectivity_1
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   ├── connectivity_2
│   │   │   ├── threshold_0.25
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.5
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   ├── threshold_0.75
│   │   │   │   ├── CHIASM [19 entries]
│   │   │   │   └── HCP [10 entries]
│   │   │   └── threshold_1
│   │   │       ├── CHIASM [19 entries]
│   │   │       └── HCP [10 entries]
│   │   └── connectivity_3
│   │       ├── threshold_0.25
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.5
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       ├── threshold_0.75
│   │       │   ├── CHIASM [19 entries]
│   │       │   └── HCP [10 entries]
│   │       └── threshold_1
│   │           ├── CHIASM [19 entries]
│   │           └── HCP [10 entries]
│   └── training_40ep_00015lr_dice
│       ├── connectivity_1
│       │   ├── threshold_0.25
│       │   │   ├── CHIASM [19 entries]
│       │   │   └── HCP [10 entries]
│       │   ├── threshold_0.5
│       │   │   ├── CHIASM [19 entries]
│       │   │   └── HCP [10 entries]
│       │   ├── threshold_0.75
│       │   │   ├── CHIASM [19 entries]
│       │   │   └── HCP [10 entries]
│       │   └── threshold_1
│       │       ├── CHIASM [19 entries]
│       │       └── HCP [10 entries]
│       ├── connectivity_2
│       │   ├── threshold_0.25
│       │   │   ├── CHIASM [19 entries]
│       │   │   └── HCP [10 entries]
│       │   ├── threshold_0.5
│       │   │   ├── CHIASM [19 entries]
│       │   │   └── HCP [10 entries]
│       │   ├── threshold_0.75
│       │   │   ├── CHIASM [19 entries]
│       │   │   └── HCP [10 entries]
│       │   └── threshold_1
│       │       ├── CHIASM [19 entries]
│       │       └── HCP [10 entries]
│       └── connectivity_3
│           ├── threshold_0.25
│           │   ├── CHIASM [19 entries]
│           │   └── HCP [10 entries]
│           ├── threshold_0.5
│           │   ├── CHIASM [19 entries]
│           │   └── HCP [10 entries]
│           ├── threshold_0.75
│           │   ├── CHIASM [19 entries]
│           │   └── HCP [10 entries]
│           └── threshold_1
│               ├── CHIASM [19 entries]
│               └── HCP [10 entries]
└── 3_DCNN_Weights

```
