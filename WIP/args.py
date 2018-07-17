import argparse


parser = argparse.ArgumentParser(description="Move robot to click")

parser.add_argument('-a', "--address",required=True,
    help = 'Specifiy IP Address of Camera')

parser.add_argument("-r", "--robot", default='onlyVision', type=str, 
    help="Com port of robot, required unless using --onlyVision")


args = vars(parser.parse_args())

if args["robot"] == 'onlyVision':
    print('yay')

print(args["address"])