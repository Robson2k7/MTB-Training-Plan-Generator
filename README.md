# MTB Training Plan Generator

MTB Training Plan Generator to aplikacja internetowa, która pozwala użytkownikom generować spersonalizowane plany treningowe dla kolarstwa górskiego (MTB). Dzięki intuicyjnemu interfejsowi aplikacja umożliwia dostosowanie planu treningowego do indywidualnych potrzeb i preferencji użytkownika.

---

## **Opis aplikacji**
Aplikacja została stworzona z wykorzystaniem nowoczesnych narzędzi, takich jak **LangFlow**, **Groq API**, model językowy **Gemma2-9b-it**, oraz framework **Streamlit**, co gwarantuje wysoką jakość generowanych planów i wygodę obsługi. 

MTB Training Plan Generator sprawdzi się zarówno dla początkujących kolarzy, jak i zaawansowanych zawodników, którzy chcą zoptymalizować swoje treningi.

---

## **Funkcjonalności**
1. **Personalizacja treningów:**
   - Możliwość wprowadzenia:
     - **Poziomu trudności:** Początkujący, Średniozaawansowany, Zaawansowany.
     - **Liczby dni treningowych w tygodniu:** od 1 do 7 dni.
     - **Tygodniowego dystansu (km):** minimalnie 10 km.
     - **Rodzaju terenu:** Górzysty, Leśny, Miejski, Mieszany.

![screen1](https://github.com/user-attachments/assets/9594d0e1-a3da-4231-b88d-fc28e6d31756)


2. **Generowanie planu:**
   - Automatyczne tworzenie szczegółowego planu treningowego MTB na podstawie danych wejściowych użytkownika.

![screen2](https://github.com/user-attachments/assets/8d3249a2-a944-4986-ba0b-5f56f2621463)


3. **Przejrzysty interfejs:**
   - Intuicyjna obsługa za pomocą formularzy, suwaków i list rozwijanych w aplikacji Streamlit.

4. **Bezpieczne przechowywanie danych:**
   - Tokeny API i dane uwierzytelniające są przechowywane w pliku `.env` i nie są udostępniane publicznie.

---

## **Technologie**
- **LangFlow:** Do zarządzania przepływem logicznym aplikacji i przetwarzania danych wejściowych.
- **Groq API:** Do integracji z modelem językowym **Gemma2-9b-it**, który generuje odpowiedzi na podstawie danych użytkownika.
- **Streamlit:** Framework do budowy nowoczesnych interfejsów aplikacji webowych.
- **Python:** Język programowania użyty do logiki aplikacji i integracji z API.
- **python-dotenv:** Biblioteka do bezpiecznego zarządzania zmiennymi środowiskowymi.

---

## **Plik `.env`**
Plik `.env` zawiera poufne dane, takie jak klucze API i tokeny uwierzytelniające, które są niezbędne do działania aplikacji. **Nie należy go udostępniać publicznie ani dodawać do systemu kontroli wersji.**

### **Przykładowa zawartość `.env`:**
```plaintext
BASE_API_URL=https://api.langflow.astra.datastax.com
LANGFLOW_ID=your_langflow_id
ENDPOINT=your_endpoint
APPLICATION_TOKEN=your_application_token
```
## **Autor**
Robson2k7

## **Licencja**
Copyright (c) 2024 Robson2k7. Wszelkie prawa zastrzeżone.

Ten projekt jest własnością prywatną. Kod źródłowy i dokumentacja są udostępnione wyłącznie do wglądu. Zabronione jest:
- Kopiowanie i rozpowszechnianie kodu.
- Modyfikowanie kodu.
- Komercyjne wykorzystanie.
- Używanie kodu lub jego części w innych projektach bez pisemnej zgody autora.

Wszelkie pytania dotyczące projektu należy kierować do autora.

-------------------------------------------------------------------------------------------------------------

# MTB Training Plan Generator

MTB Training Plan Generator is a web application that allows users to generate personalized training plans for mountain biking (MTB). Thanks to its intuitive interface, the application enables users to customize their training plans to suit their individual needs and preferences.

---

## **Application Overview**
The application was created using modern tools such as **LangFlow**, **Groq API**, the **Gemma2-9b-it** language model, and the **Streamlit** framework, ensuring high-quality training plans and ease of use.

MTB Training Plan Generator is suitable for both beginner cyclists and advanced riders who want to optimize their training.

---

## **Features**
1. **Training Personalization:**
   - The ability to input:
     - **Difficulty level:** Beginner, Intermediate, Advanced.
     - **Number of training days per week:** From 1 to 7 days.
     - **Weekly distance (km):** Minimum 10 km.
     - **Terrain type:** Mountainous, Forest, Urban, Mixed.

2. **Plan Generation:**
   - Automatically generates a detailed MTB training plan based on user input.

3. **User-Friendly Interface:**
   - Intuitive handling through forms, sliders, and dropdown menus in the Streamlit application.

4. **Secure Data Storage:**
   - API tokens and authentication data are stored in a `.env` file and are not publicly shared.

---

## **Technologies**
- **LangFlow:** For managing the application's logical flow and processing user inputs.
- **Groq API:** For integration with the **Gemma2-9b-it** language model, which generates responses based on user data.
- **Streamlit:** Framework for building modern web application interfaces.
- **Python:** The programming language used for application logic and API integration.
- **python-dotenv:** Library for securely managing environment variables.

---

## **`.env` File**
The `.env` file contains sensitive data such as API keys and authentication tokens that are essential for the application's functionality. **It should not be shared publicly or added to version control.**

### **Example `.env` File:**
```plaintext
BASE_API_URL=https://api.langflow.astra.datastax.com
LANGFLOW_ID=your_langflow_id
ENDPOINT=your_endpoint
APPLICATION_TOKEN=your_application_token
```

## **Author**
Robson2k7

## **License**

Copyright (c) 2024 Robson2k7. All rights reserved.

This project is private property. The source code and documentation are provided for viewing purposes only. The following actions are prohibited:

- Copying and distributing the code.
- Modifying the code.
- Commercial use.
- Using the code or any part of it in other projects without the written consent of the author.

All inquiries regarding the project should be directed to the author.
