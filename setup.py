#!/usr/bin/env python3
"""
Configuration and Setup for Quarto Presentation Generator
"""

import os
import sys
from pathlib import Path

class Config:
    """Configuration settings for the presentation generator"""
    
    # Default settings
    DEFAULT_SLIDES = 20
    DEFAULT_MODEL = "gpt-4"
    DEFAULT_THEME = "default"
    
    # File paths
    PROJECT_ROOT = Path(__file__).parent
    PROMPT_TEMPLATE_PATH = PROJECT_ROOT / "prompt_template.md"
    
    # LLM Provider settings
    OPENAI_MODELS = ["gpt-4", "gpt-4-turbo-preview", "gpt-3.5-turbo"]
    ANTHROPIC_MODELS = ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
    
    # Quarto themes
    QUARTO_THEMES = [
        "default", "dark", "beige", "blood", "dracula", 
        "league", "moon", "night", "serif", "simple", 
        "sky", "solarized"
    ]
    
    @staticmethod
    def check_dependencies():
        """Check if required dependencies are installed"""
        dependencies = {
            "required": ["json", "os", "datetime", "argparse"],
            "optional": {
                "openai": "OpenAI integration",
                "anthropic": "Anthropic Claude integration", 
                "requests": "Local LLM integration",
                "python-dotenv": "Environment variable loading"
            }
        }
        
        print("🔍 Checking dependencies...")
        
        # Check required dependencies
        for dep in dependencies["required"]:
            try:
                __import__(dep)
                print(f"✅ {dep} - Available")
            except ImportError:
                print(f"❌ {dep} - Missing (required)")
                return False
        
        # Check optional dependencies
        for dep, description in dependencies["optional"].items():
            try:
                __import__(dep)
                print(f"✅ {dep} - Available ({description})")
            except ImportError:
                print(f"⚠️  {dep} - Not installed ({description})")
        
        return True
    
    @staticmethod
    def check_api_keys():
        """Check if API keys are configured"""
        print("\n🔑 Checking API keys...")
        
        keys = {
            "OPENAI_API_KEY": "OpenAI GPT models",
            "ANTHROPIC_API_KEY": "Anthropic Claude models"
        }
        
        found_keys = 0
        for key, description in keys.items():
            if os.getenv(key):
                print(f"✅ {key} - Configured ({description})")
                found_keys += 1
            else:
                print(f"❌ {key} - Not set ({description})")
        
        if found_keys == 0:
            print("\n⚠️  No API keys found. The script will use placeholder responses.")
            print("Set API keys to enable real LLM integration:")
            print("  export OPENAI_API_KEY='your-key-here'")
            print("  export ANTHROPIC_API_KEY='your-key-here'")
        
        return found_keys > 0
    
    @staticmethod
    def setup_environment():
        """Set up the environment for first-time use"""
        print("🚀 Setting up Quarto Presentation Generator...")
        
        # Check Python version
        if sys.version_info < (3, 8):
            print("❌ Python 3.8+ required")
            return False
        
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        
        # Check dependencies
        if not Config.check_dependencies():
            print("\n📦 Install missing dependencies:")
            print("  pip install -r requirements.txt")
            return False
        
        # Check API keys
        Config.check_api_keys()
        
        # Check if Quarto is installed
        print("\n🔧 Checking Quarto installation...")
        try:
            import subprocess
            result = subprocess.run(["quarto", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Quarto {result.stdout.strip()} installed")
            else:
                print("❌ Quarto not found")
                print("Install Quarto: https://quarto.org/docs/get-started/")
                return False
        except FileNotFoundError:
            print("❌ Quarto not found in PATH")
            print("Install Quarto: https://quarto.org/docs/get-started/")
            return False
        
        print("\n✅ Environment setup complete!")
        return True
    
    @staticmethod
    def create_sample_files():
        """Create sample files for testing"""
        samples_created = []
        
        # Sample .env file
        env_file = Config.PROJECT_ROOT / ".env.example"
        if not env_file.exists():
            with open(env_file, "w") as f:
                f.write("# API Keys for LLM integration\n")
                f.write("OPENAI_API_KEY=your-openai-api-key-here\n")
                f.write("ANTHROPIC_API_KEY=your-anthropic-api-key-here\n")
            samples_created.append(".env.example")
        
        # Sample configuration
        config_file = Config.PROJECT_ROOT / "config.json"
        if not config_file.exists():
            config_data = {
                "default_model": Config.DEFAULT_MODEL,
                "default_slides": Config.DEFAULT_SLIDES,
                "default_theme": Config.DEFAULT_THEME,
                "output_directory": "output/",
                "templates": {
                    "academic": {
                        "theme": "serif",
                        "transition": "fade",
                        "code_line_numbers": True
                    },
                    "business": {
                        "theme": "simple", 
                        "transition": "slide",
                        "incremental": True
                    },
                    "technical": {
                        "theme": "dark",
                        "transition": "convex",
                        "chalkboard": True
                    }
                }
            }
            
            import json
            with open(config_file, "w") as f:
                json.dump(config_data, f, indent=2)
            samples_created.append("config.json")
        
        if samples_created:
            print(f"\n📄 Created sample files: {', '.join(samples_created)}")
        
        return samples_created


def main():
    """Main setup function"""
    print("=" * 60)
    print("  QUARTO PRESENTATION GENERATOR SETUP")
    print("=" * 60)
    
    if Config.setup_environment():
        Config.create_sample_files()

        print("\n🎉 Setup complete! Ready to generate presentations.")
        print("\nQuick start:")
        print("  python presentation_generator.py your_article.txt")
        print("\nFor help:")
        print("  python presentation_generator.py --help")
    else:
        print("\n❌ Setup incomplete. Please address the issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
