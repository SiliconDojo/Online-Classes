## For Web Cam Code

You may have to swictch --camera default to either 0, or 1 depending on your computer

#SDNOTE -- default= should be wither 0 or 1. 0 is default. 1 needed for ARM Macs
parser.add_argument('--camera', help='Camera divide number.', type=int, default=1)