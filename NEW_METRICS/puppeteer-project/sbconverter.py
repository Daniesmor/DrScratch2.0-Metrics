import zipfile
import json
import sys

def convert_sb2_to_sb3(sb2_path, sb3_path):
    with zipfile.ZipFile(sb2_path, 'r') as sb2_zip:
        with sb2_zip.open('project.json') as sb2_json_file:
            project_data = json.load(sb2_json_file)
            
            print(project_data)
        
        # La estructura del proyecto debe ser adaptada a la especificación de Scratch 3.0
        project_data['targets'] = project_data.pop('children', [])
        
        for target in project_data['targets']:
            if 'scripts' in target:
                target['blocks'] = {}
                for script in target.pop('scripts'):
                    # Convertir los scripts a bloques en el formato de Scratch 3.0
                    for block in script[2]:
                        if len(block) < 2:
                            print(f"Bloque con datos insuficientes: {block}")
                            continue
                        
                        block_id = block.pop(0)
                        block_type = block.pop(0)
                        block_data = block
                        target['blocks'][block_id] = {
                            "opcode": block_type,
                            "next": None,
                            "parent": None,
                            "inputs": {},
                            "fields": {},
                            "shadow": False,
                            "topLevel": True,
                            "x": 0,
                            "y": 0
                        }
        
        with zipfile.ZipFile(sb3_path, 'w') as sb3_zip:
            sb3_zip.writestr('project.json', json.dumps(project_data, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sbconverter.py <input.sb2> <output.sb3>")
    else:
        input_sb2 = sys.argv[1]
        output_sb3 = sys.argv[2]
        convert_sb2_to_sb3(input_sb2, output_sb3)

