import argparse

from options import _aws

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start IoT Services.')
    parser.add_argument('--provider', '-p', type=int, default=1,
                        help='Provide the key for the service to be \
                            initialized. \n1- AWS IoT Core')

    args = parser.parse_args()

    if args.provider == 1:
        aws_service = _aws()
        aws_service.run()
    else:
        raise NotImplementedError("Provide a valid option")