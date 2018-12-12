# FIXME. hardcoded "build" directory in env-vars.sh file
BUILD_DIR="build"

.PHONY: all clean

all:
	./get-opis.sh

clean:
	rm -rf ${BUILD_DIR}
