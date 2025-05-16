student = {"meno": "Eva", "vek":17, "predmet":["matika","smarty"]}

student["telefon"] = "555523"
student["meno"] = "Mora"

print(student.get("meno", "nenašlo"))