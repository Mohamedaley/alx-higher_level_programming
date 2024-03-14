#!/usr/bin/python3
if __name__ == "__main__":
    import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.info("This is a logged message")
