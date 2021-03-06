#
# modules/properties/Makefile
#
# Build the iRODS embedPython module
#

ifndef buildDir
buildDir = $(CURDIR)/../..
endif

include $(buildDir)/config/config.mk
include $(buildDir)/config/platform.mk
include $(buildDir)/config/directories.mk
include $(buildDir)/config/common.mk

#
# Directories
#
MSObjDir =	$(modulesDir)/embedPython/microservices/obj
MSSrcDir =	$(modulesDir)/embedPython/microservices/src
MSIncDir =	$(modulesDir)/embedPython/microservices/include

# Python 
PYTHON_VERSION = 2.7
PYTHON_PATH = /usr
PYTHON_OBJECTS = $(PYTHON_PATH)/lib/libpython$(PYTHON_VERSION).so
# Include files and libraries for python.
# Please run 'python-config --ldflags'
# on your system and edit the following 2 lines accordingly.
PYTHON_INCLUDE = -I$(PYTHON_PATH)/include/python$(PYTHON_VERSION) -fno-strict-aliasing \
				 -DNDEBUG -g -fwrapv -O3 -Wall
PYTHON_LIBS = -lpthread -ldl -lutil -lm

# PyRods
PYRODS_PATH = /home/rods/install/PyRods
PYRODS_INCLUDE = -I$(PYRODS_PATH)/include
PYRODS_OBJECTS = $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyMsParam.o \
                 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyDataObj.o \
                 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyGetRodsEnv.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRcConnect.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRodsDef.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRodsError.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRodsFile.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRodsExec.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRodsInfo.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/PyRodsUser.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/sqlMisc.o \
 		  		 $(PYRODS_PATH)/build/temp.linux-i686-$(PYTHON_VERSION)/src/wrapper_misc.o

#
# Source files
#
MSOBJECT = $(MSObjDir)/embedPythonMS.o
OBJECTS = $(MSOBJECT) $(PYRODS_OBJECTS)

INCLUDE_FLAGS =	-I$(MSIncDir) $(PYTHON_INCLUDE) $(PYRODS_INCLUDE)
#
# Compile and link flags
#
INCLUDES +=	$(INCLUDE_FLAGS) $(LIB_INCLUDES) $(SVR_INCLUDES)
CFLAGS_OPTIONS := -DRODS_SERVER $(CFLAGS) $(MY_CFLAG)
CFLAGS := $(CFLAGS_OPTIONS) $(INCLUDES) $(MODULE_CFLAGS)



.PHONY: all rules microservices server client clean
.PHONY: server_ldflags client_ldflags server_cflags client_cflags
.PHONY: print_cflags

# Build everything
all:	microservices
	@true

# List module's objects for inclusion in the clients
client_ldflags:
	@true

# List module's includes for inclusion in the clients
client_cflags:
	@true

# List module's objects for inclusion in the server
server_ldflags:
	@echo $(OBJECTS) $(PYTHON_OBJECTS) $(PYTHON_LIBS)

# List module's includes for inclusion in the server
server_cflags:
	@echo $(INCLUDE_FLAGS)

# Build microservices
microservices:	print_cflags $(OBJECTS)
	@true

# Build client additions
client:
	@true

# Build server additions
server:
	@true

# Build rules
rules:
	@true

# Clean
clean:
	@echo "Clean embedPython module..."
	@rm -f $(MSOBJECT)


# Show compile flags
print_cflags:
	@echo "Compile flags:"
	@echo "    $(CFLAGS_OPTIONS)"


#
# Compilation targets
#
$(MSOBJECT): $(MSObjDir)/%.o: $(MSSrcDir)/%.c $(DEPEND)
	@echo "Compile embedPython module `basename $@`..."
	@$(CC) -c $(CFLAGS) -o $@ $<
