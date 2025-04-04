# A test of the NumaTTS class, without implementing the api (making testing faster)

from numa_speak import NumaTTS
import sys

if __name__ == "__main__":
    # Default text or command-line input
    text = (
        "This is a local test of the NumaTTS system with high pitch voice."
    )
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])

    numa = NumaTTS(highPitch_mode=True)
    numa.say(text)