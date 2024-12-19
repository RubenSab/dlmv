SCRIPT_NAME=dlmv.py
INSTALL_DIR=/usr/local/bin
TARGET=$(INSTALL_DIR)/dlmv

# Default action
all:
	@echo "Run 'make install' to install $(SCRIPT_NAME)."

# Install the script
install:
	@echo "Installing $(SCRIPT_NAME) to $(INSTALL_DIR)..."
	chmod +x $(SCRIPT_NAME)
	sudo cp $(SCRIPT_NAME) $(TARGET)
	@echo "Installation complete! You can now use 'dlmv' as a command."

# Uninstall the script
uninstall:
	@echo "Removing $(TARGET)..."
	sudo rm -f $(TARGET)
	@echo "Uninstallation complete."
