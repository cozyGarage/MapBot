#!/usr/bin/env python
"""
Basic tests for MapBot functionality without database dependencies
"""
import sys
sys.path.insert(0, '.')

def test_imports():
    """Test that all modules can be imported"""
    print("Testing module imports...")
    try:
        import utilities
        print("  ✓ utilities")
        import features
        print("  ✓ features")
        import googleMapsApiModule
        print("  ✓ googleMapsApiModule")
        import chatbot
        print("  ✓ chatbot")
        return True
    except Exception as e:
        print(f"  ✗ Import failed: {e}")
        return False

def test_parse_sentence():
    """Test spaCy-based sentence parsing"""
    print("\nTesting sentence parsing...")
    try:
        from utilities import parse_sentence
        
        test_sentences = [
            "Where is the nearest restaurant?",
            "How do I get to the airport?",
            "Show me directions to New York"
        ]
        
        for sentence in test_sentences:
            triples, root = parse_sentence(sentence)
            print(f"  '{sentence}'")
            print(f"    Root: {root}, Triples: {len(triples)}")
        
        return True
    except Exception as e:
        print(f"  ✗ Parse failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_features():
    """Test feature extraction"""
    print("\nTesting feature extraction...")
    try:
        import features
        
        test_sentence = "Where is the nearest restaurant?"
        result = features.features_dict('test123', test_sentence, 'Q')
        
        print(f"  Extracted {len(result)} features")
        print(f"  Word count: {result['wordCount']}")
        print(f"  Question mark: {result['qMark']}")
        print(f"  Classification: {result['class']}")
        
        return True
    except Exception as e:
        print(f"  ✗ Features failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_classification():
    """Test sentence classification"""
    print("\nTesting sentence classification...")
    try:
        from utilities import classify_model, classify_sentence
        
        clf = classify_model()
        print("  Model loaded")
        
        test_cases = [
            ("How are you?", "Chat/Question"),
            ("Hello there", "Chat"),
            ("Where is Times Square?", "Question"),
        ]
        
        for sentence, expected in test_cases:
            classification = classify_sentence(clf, sentence)
            print(f"  '{sentence}' → {classification}")
        
        return True
    except Exception as e:
        print(f"  ✗ Classification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_nltk_setup():
    """Test NLTK data availability"""
    print("\nTesting NLTK setup...")
    try:
        from utilities import setup_nltk
        setup_nltk()
        print("  ✓ NLTK data available")
        return True
    except Exception as e:
        print(f"  ✗ NLTK setup failed: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("MapBot Basic Functionality Tests (2025 Edition)")
    print("=" * 60)
    
    results = []
    results.append(("Module Imports", test_imports()))
    results.append(("NLTK Setup", test_nltk_setup()))
    results.append(("Sentence Parsing", test_parse_sentence()))
    results.append(("Feature Extraction", test_features()))
    results.append(("Classification", test_classification()))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    all_passed = all(result[1] for result in results)
    print("\n" + ("All tests passed! ✓" if all_passed else "Some tests failed ✗"))
    
    sys.exit(0 if all_passed else 1)
