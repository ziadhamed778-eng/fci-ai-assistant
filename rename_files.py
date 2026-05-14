import os

# المسار الرئيسي بتاعك
base_path = r"C:\Users\MSI\Desktop\مواد\مواد is"

print("🔍 جاري فحص المجلدات...\n" + "-"*30)
files_renamed = 0

for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    # التأكد إن ده فولدر مش ملف
    if os.path.isdir(folder_path):
        course_code = folder_name.upper().strip()
        print(f"📂 دخلت فولدر: {course_code}")
        
        for filename in os.listdir(folder_path):
            # التأكد إن الملف PDF
            if filename.lower().endswith(".pdf"):
                # استخراج أي رقم موجود في اسم الملف
                lecture_number = ''.join(filter(str.isdigit, filename))
                
                if lecture_number:
                    new_name = f"{course_code}_Lec{lecture_number}.pdf"
                    old_file = os.path.join(folder_path, filename)
                    new_file = os.path.join(folder_path, new_name)
                    
                    # لو الاسم لسة متغيرش، غيره
                    if filename != new_name:
                        os.rename(old_file, new_file)
                        print(f"  ✅ تم تغيير: {filename} ---> {new_name}")
                        files_renamed += 1
                    else:
                        print(f"  ⚡ الملف {filename} متسمي صح بالفعل.")
                else:
                    print(f"  ❌ مقدرتش ألاقي رقم في اسم الملف: {filename}")
            else:
                print(f"  ⚠️ تم تخطي ملف (مش بصيغة PDF): {filename}")
        print("-" * 20)

if files_renamed > 0:
    print(f"\n🎉 تمت العملية بنجاح! تم تغيير اسم {files_renamed} ملف.")
else:
    print("\n🤔 السكريبت مغيرش أي حاجة! شوف الرسايل اللي فوق عشان تعرف السبب.")