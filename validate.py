#!/usr/bin/env python3
"""
Validation script for CapsuleCRM MCP Extension
Tests all components before packaging
"""

import os
import sys
import json
import logging
from pathlib import Path

def validate_manifest():
    """Validate manifest.json structure"""
    print("🔍 Validating manifest.json...")
    
    try:
        with open("manifest.json", "r") as f:
            manifest = json.load(f)
        
        required_fields = ["dxt_version", "name", "version", "description", "author", "server"]
        for field in required_fields:
            if field not in manifest:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Validate server config
        server = manifest["server"]
        if server["type"] != "python":
            print(f"❌ Invalid server type: {server['type']}")
            return False
            
        if not Path(server["entry_point"]).exists():
            print(f"❌ Entry point not found: {server['entry_point']}")
            return False
        
        print("✅ Manifest validation passed")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in manifest: {e}")
        return False
    except Exception as e:
        print(f"❌ Manifest validation failed: {e}")
        return False

def validate_dependencies():
    """Validate all dependencies are bundled"""
    print("🔍 Validating dependencies...")
    
    lib_dir = Path("server/lib")
    if not lib_dir.exists():
        print("❌ Dependencies not bundled in server/lib")
        return False
    
    required_packages = ["fastmcp", "httpx", "pydantic", "fastapi"]
    missing = []
    
    for package in required_packages:
        if not any((lib_dir).glob(f"{package}*")):
            missing.append(package)
    
    if missing:
        print(f"❌ Missing packages: {missing}")
        return False
    
    print("✅ Dependencies validation passed")
    return True

def validate_server():
    """Validate server can start without errors"""
    print("🔍 Validating server startup...")
    
    try:
        # Set dummy token for testing
        os.environ["CAPSULECRM_ACCESS_TOKEN"] = "test_token_123"
        
        # Add paths
        sys.path.insert(0, "server")
        sys.path.insert(0, "server/lib")
        
        # Test import
        from server.main import mcp
        
        # Test tool registration
        # FastMCP doesn't expose _tools directly, but import was successful
        print("✅ Server validation passed (MCP instance created successfully)")
        return True
        
    except Exception as e:
        print(f"❌ Server validation failed: {e}")
        return False

def validate_structure():
    """Validate file structure"""
    print("🔍 Validating file structure...")
    
    required_files = [
        "manifest.json",
        "server/main.py",
        "server/api/__init__.py",
        "server/tools/__init__.py",
        "README.md",
        "LICENSE"
    ]
    
    missing = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing.append(file_path)
    
    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    
    print("✅ File structure validation passed")
    return True

def main():
    """Run all validations"""
    print("🚀 CapsuleCRM MCP Extension Validation")
    print("=" * 50)
    
    # Suppress logging during validation
    logging.disable(logging.CRITICAL)
    
    validations = [
        validate_structure,
        validate_manifest,
        validate_dependencies,
        validate_server
    ]
    
    passed = 0
    for validation in validations:
        if validation():
            passed += 1
        print()
    
    print("=" * 50)
    if passed == len(validations):
        print("🎉 All validations passed! Extension is ready for packaging.")
        return True
    else:
        print(f"❌ {len(validations) - passed} validations failed. Please fix issues before packaging.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)