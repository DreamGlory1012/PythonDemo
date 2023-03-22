"""
    Author: AubreyChen
    Time: 2023/3/19 16:18
    File: contactcms.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import os
import pickle


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = []

    def save_contacts(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.contacts, f)

    def load_contacts(self, filename):
        with open(filename, 'rb') as f:
            self.contacts = pickle.load(f)

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"姓名：{contact.name}，电话：{contact.phone}，电子邮件：{contact.email}")
                return
        print("未找到该联系人！")

    def update_contact(self, name, phone, email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                print("联系人信息已更新！")
                return
        print("未找到该联系人！")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("联系人已删除！")
                return
        print("未找到该联系人！")

def main():
    contacts = ContactList()
    # 检查是否存在以前保存的联系人列表文件
    filename = 'contacts.pkl'
    if os.path.exists(filename):
        contacts.load_contacts(filename)
    while True:
        print("欢迎使用手机通讯录管理系统！")
        print("1. 添加联系人")
        print("2. 查找联系人")
        print("3. 修改联系人")
        print("4. 删除联系人")
        print("5. 退出系统")
        choice = input("请选择操作（1/2/3/4/5）：")
        if choice == "1":
            name = input("请输入姓名：")
            phone = input("请输入电话：")
            email = input("请输入电子邮件：")
            contacts.add_contact(name, phone, email)
            print("联系人已添加！")
        elif choice == "2":
            name = input("请输入要查找的联系人姓名：")
            contacts.search_contact(name)
        elif choice == "3":
            name = input("请输入要修改的联系人姓名：")
            phone = input("请输入新的电话：")
            email = input("请输入新的电子邮件：")
            contacts.update_contact(name, phone, email)
        elif choice == "4":
            name = input("请输入要删除的联系人姓名：")
            contacts.delete_contact(name)
        elif choice == '5':
            # 保存联系人列表并退出程序
            contacts.save_contacts(filename)
            print("程序已退出。")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()
