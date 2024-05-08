#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas


# In[13]:


def load_data(csv_file):
    return pd.read_csv("C:/Users/saiku/Downloads/IDs.csv")


def create_id_card(template_path, photo_path, name, title, output_path):
    try:
      
        template = Image.open("C:/Users/saiku/OneDrive/Desktop/ImagesforID/ute_id_template.png").convert("RGBA")
        photo = Image.open(photo_path).resize((100, 100)) 
        
       
        template.paste(photo, (50, 60))  
        draw = ImageDraw.Draw(template)
        font = ImageFont.load_default()
      
        draw.text((160, 70), name, font=font, fill="black")
        draw.text((160, 120), title, font=font, fill="black")
        
        template.save(output_path)
        return output_path
    except Exception as e:
        print(f"Error creating ID card: {e}")
        return None


# In[14]:


def create_pdf(csv_file, template_img, pdf_file):
    data = load_data(csv_file)
    c = canvas.Canvas(pdf_file)
    
    for index, row in data.iterrows():
        img_path = create_id_card(template_img, row['Photo'], row['Name'], row['Title'], f"temp_{index}.png")
        if img_path:
            c.setPageSize((612, 792))  # Standard letter size: 8.5 x 11 inches (612 x 792 points)
            c.drawImage(img_path, 0, 0, width=612, height=792)
            c.showPage()
            os.remove(img_path)  # Clean up temp file
    
    c.save()


if __name__ == "__main__":
    csv_file_path = "employees.csv"
    template_image_path = "ute_id_template.png"
    output_pdf_file = "employee_ids.pdf"
    
    create_pdf(csv_file_path, template_image_path, output_pdf_file)


# In[ ]:




