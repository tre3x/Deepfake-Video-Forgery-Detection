import argparse
from train import train

def main():
    parser = argparse.ArgumentParser(description='Visual Attention based Deepfake Video Forgery Detection')

    parser.add_argument('--train', type=str, nargs = '+', help = 'What is the path of the training image data?')
    parser.add_argument('--val', type=str, nargs = '+', help = 'What is the path of the Validation image data?')
    parser.add_argument('--epochs', type=int, default=50, help = 'What is the training epoch for model?')
    parser.add_argument('--batch', type=int, default=32, help = 'What is the training batch size?')
    parser.add_argument('--steps', type=int, default=40, help = 'What is the training steps per epoch?')

    args = parser.parse_args()
    args.train = ' '.join(args.train)
    args.val = ' '.join(args.val)

    print("Configuration")
    print("----------------------------------------------------------------------")
    print("Training Path : {}".format(args.train))
    print("Validation Path : {}".format(args.val))
    print("Epochs while training the model : {}".format(args.epochs))
    print("Batch Size : {}".format(args.batch))
    print("Steps per epochs : {}".format(args.steps))
    print("----------------------------------------------------------------------")

    train(args.train, args.val).run(args.epochs, args.batch, args.steps)

if __name__=='__main__':
    main()