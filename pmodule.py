import pandas as pd

FILE_NAME='order.csv'

def initialize():
    try:
        df=pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        df=pd.DataFrame(columns=['Ім\'я клієнта','Номер замовлення', 'Дата замовлення', 'Сума замовлення', 'Статус' ])
        df.to_csv(FILE_NAME,index=False)

def load():
    try:
        return pd.read_csv(FILE_NAME)
    except Exception as e:
        print(f"Помилка. Не вдалося завантажити файл({e})")
        return pd.DataFrame(columns=['Ім\'я клієнта','Номер замовлення', 'Дата замовлення', 'Сума замовлення', 'Статус' ])

def save(df):
    try:
        df.to_csv(FILE_NAME,index=False)
    except Exception as e:
        print(f'Помилка. Не вдалося зберегти файл ({e})')

def add(df):
    name = input("Введіть ім'я клієнта: ")
    try:
        num = int(input("Введіть номер замовлення: "))
        price = float(input("Введіть суму замовлення: "))
        date = int(input("Введіть дату замовлення: "))
    except ValueError:
        print("Помилка. Ціна, Номер та Дата замовлення мають бути числами. ")
        return df
    status = input("Введіть статус замовлення: ")
    if (not name or not status):
        print("Ім'я клієнта та статус замовлення не можуть бути порожніми.")
        return df
    order = {"Ім'я клієнта": name,'Номер замовлення':num,'Дата замовлення':date,'Сума замовлення':price,'Статус':status}
    df = df.append(order, ignore_index=True)
    return df

def edit(df):
    num = input("Введіть номер замовлення, яке потрібно змінити : ")
    if name not in df["Номер замовлення"].values:
        print("Замовлення не знайдено!")
        return df

    idx = df[df["Ім'я клієнта"] == name].index[0]
    print(f"Поточні дані: {df.loc[idx]}")

    name = input("Введіть нове ім'я клієнта (залиште порожнім, щоб не змінювати): ")
    try:
        date = input("Нова дата замовлення (залиште порожнім, щоб не змінювати): ")
        price = input("Нова ціна замовлення (залиште порожнім, щоб не змінювати): ")
        status = input("Новий статус замовлення (залиште порожнім, щоб не змінювати): ")
        if name:
            df.at[idx, "Ім'я клієнта"] = name
        if date:
            df.at[idx, "Дата замовлення"] = int(date)
        if price:
            df.at[idx, "Сума замовлення"] = float(price)
        if (status=="В процесі" or status=="Виконано"):
            df.at[idx, "Статус"] = status
        save(df)
        print("Замовлення успішно змінено!")
    except ValueError:
        print("Дата та сума замовлення мають бути числами!")
    return df

def delete(df):
    num = input("Введіть номер замовлення, який потрібно видалити: ")
    if num not in df["Номер замовлення"].values:
        print("Замовлення не знайдено!")
        return df

    df = df[df["Номер замовлення"] != num]
    save(df)
    print("Замовлення успішно видалено!")
    return df

def display(df):
    if df.empty:
        print("Дані відсутні.")
    else:
        print(df.to_string(index=False))

def sum(df):
    print(f"Загальна сума замовленнь: {df['Сума замовлення'].sum()}")

initialize()
data = load()

while True:
    print("\nМеню:")
    print("1. Показати всі замовлення")
    print("2. Додати замовлення")
    print("3. Редагувати замовлення")
    print("4. Видалити замовлення")
    print("5. Загальна вартість замовленнь")
    
    print("0. Вийти")
    choice = input("Оберіть дію: ")
    if choice == "1":
        display(data)
    elif choice == "2":
        data = add(data)
    elif choice == "3":
        data = edit(data)
    elif choice == "4":
        data = delete(data)
    elif choice == "5":
        sum(data)
    
    elif choice == "0":
        print("Вихід із програми.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")