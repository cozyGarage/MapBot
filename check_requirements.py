#!/usr/bin/env python
"""
Check if system meets MapBot 2025 requirements
"""
import sys

def check_python_version():
    """Check if Python version is 3.10 or higher"""
    major, minor = sys.version_info[:2]
    print(f"Python Version: {major}.{minor}.{sys.version_info.micro}")
    
    if (major, minor) >= (3, 10):
        print("  ✓ Python version is compatible")
        return True
    else:
        print(f"  ✗ Python 3.10+ required (you have {major}.{minor})")
        return False

def check_packages():
    """Check if required packages are installed"""
    required_packages = [
        ('googlemaps', '4.10.0'),
        ('nltk', '3.9.1'),
        ('pandas', '2.2.3'),
        ('numpy', '2.1.3'),
        ('sklearn', '1.5.2'),
        ('mysql.connector', '9.1.0'),
        ('spacy', '3.8.2'),
    ]
    
    all_good = True
    print("\nRequired Packages:")
    
    for package_name, min_version in required_packages:
        try:
            if package_name == 'sklearn':
                import sklearn
                version = sklearn.__version__
            elif package_name == 'mysql.connector':
                import mysql.connector
                version = mysql.connector.__version__
            else:
                pkg = __import__(package_name)
                version = pkg.__version__
            
            print(f"  ✓ {package_name} {version}")
        except ImportError:
            print(f"  ✗ {package_name} not installed")
            all_good = False
        except AttributeError:
            print(f"  ? {package_name} installed (version unknown)")
    
    return all_good

def check_spacy_model():
    """Check if spaCy English model is installed"""
    print("\nspaCy Model:")
    try:
        import spacy
        nlp = spacy.load('en_core_web_sm')
        print(f"  ✓ en_core_web_sm loaded successfully")
        return True
    except OSError:
        print(f"  ✗ en_core_web_sm not found")
        print(f"    Run: python -m spacy download en_core_web_sm")
        return False
    except Exception as e:
        print(f"  ✗ Error loading model: {e}")
        return False

def check_nltk_data():
    """Check if NLTK data is available"""
    print("\nNLTK Data:")
    required_data = ['punkt', 'punkt_tab', 'averaged_perceptron_tagger', 
                     'averaged_perceptron_tagger_eng', 'stopwords', 'wordnet']
    
    all_good = True
    try:
        import nltk
        for dataset in required_data:
            try:
                nltk.data.find(f'tokenizers/{dataset}' if 'punkt' in dataset or 'tagger' in dataset 
                              else f'corpora/{dataset}' if dataset in ['stopwords', 'wordnet']
                              else dataset)
                print(f"  ✓ {dataset}")
            except LookupError:
                print(f"  ✗ {dataset} not found")
                all_good = False
    except ImportError:
        print("  ✗ NLTK not installed")
        all_good = False
    
    if not all_good:
        print("    Run setup_nltk() from utilities.py or the init.py script")
    
    return all_good

def check_database():
    """Check if MySQL is available"""
    print("\nDatabase:")
    try:
        import mysql.connector
        print("  ✓ MySQL connector available")
        print("    Note: You still need to create the 'mapbot' database")
        print("    Run: mysql -uroot -p -hlocalhost")
        print("         CREATE DATABASE mapbot;")
        return True
    except ImportError:
        print("  ✗ MySQL connector not installed")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("MapBot 2025 Requirements Check")
    print("=" * 60)
    print()
    
    checks = []
    checks.append(check_python_version())
    checks.append(check_packages())
    checks.append(check_spacy_model())
    checks.append(check_nltk_data())
    checks.append(check_database())
    
    print("\n" + "=" * 60)
    if all(checks):
        print("✓ All requirements met! You're ready to run MapBot.")
        print("\nRun: python init.py")
    else:
        print("✗ Some requirements are missing. Please install them:")
        print("\n  pip install -r requirements.txt")
        print("  python -m spacy download en_core_web_sm")
        print("\nThen run this check again.")
    print("=" * 60)
