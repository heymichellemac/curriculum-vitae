.PHONY: build install clean serve help venv

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

# Default target
all: build

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "Virtual environment created!"

# Install dependencies
install: venv
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed!"

# Build the CV
build: install
	@echo "Building CV..."
	$(PYTHON) generate.py

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -f index.html
	rm -f out/*.html

# Deep clean (remove venv too)
clean-all: clean
	@echo "Removing virtual environment..."
	rm -rf $(VENV)

# Serve locally (requires Python's http.server)
serve: build
	@echo "Starting local server at http://localhost:8000"
	@echo "Press Ctrl+C to stop"
	$(PYTHON) -m http.server 8000

# Show help
help:
	@echo "CV Generator - Makefile targets:"
	@echo ""
	@echo "  make install    Create venv and install Python dependencies"
	@echo "  make build      Generate CV from YAML data"
	@echo "  make clean      Remove generated files"
	@echo "  make clean-all  Remove generated files and virtual environment"
	@echo "  make serve      Build and serve CV locally at localhost:8000"
	@echo "  make help       Show this help message"
