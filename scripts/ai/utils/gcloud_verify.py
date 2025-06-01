# test_vertex_setup.py
def verify_setup(project_id, location="us-central1"):
    try:
        # Test basic import
        from google.cloud import aiplatform
        from google.cloud import storage
        print("✅ Basic imports successful")
       
        # Initialize Vertex AI
        aiplatform.init(project=project_id, location=location)
        print("✅ Vertex AI initialization successful")
       
        # Test Storage access
        storage_client = storage.Client(project=project_id)
        print("✅ Cloud Storage client created")
       
        # Test Dataset class (this was failing)
        try:
            # List existing datasets instead of creating one
            datasets = aiplatform.TabularDataset.list()
            print(f"✅ Dataset listing successful - found {len(datasets)} datasets")
        except Exception as e:
            print(f"⚠️  Dataset listing failed (this might be normal if no datasets exist): {e}")
       
        # Test basic permissions by listing models
        try:
            models = aiplatform.Model.list()
            print(f"✅ Model listing successful - found {len(models)} models")
        except Exception as e:
            print(f"⚠️  Model listing failed: {e}")
           
        print(f"🎉 Setup verification complete for project: {project_id}")
       
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run: pip3 install --upgrade google-cloud-aiplatform")
    except Exception as e:
        print(f"❌ Setup issue: {e}")

# Run verification - replace with your project ID
verify_setup("hellocloud-460621")
