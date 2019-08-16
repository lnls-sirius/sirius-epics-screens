# Default PROJECT variable
PROJECT ?= "all"

EXTRA_OPTS =

ifneq ($(PROJECT),)
	EXTRA_OPTS += -p $(PROJECT)
else
	EXTRA_OPTS +=
endif

ifneq ($(BUILD_DIR),)
	EXTRA_OPTS += -b $(BUILD_DIR)
else
	EXTRA_OPTS +=
endif

ifneq ($(IOC_REPO_DIR),)
	EXTRA_OPTS += -r $(IOC_REPO_DIR)
else
	EXTRA_OPTS +=
endif

ifneq ($(OPI_DIR),)
	EXTRA_OPTS += -o $(OPI_DIR)
else
	EXTRA_OPTS +=
endif

.PHONY: all clean

all:
	./get-opis.sh $(EXTRA_OPTS)

clean: BUILD_DIR ?= "build"
clean:
	rm -rf $(BUILD_DIR)
