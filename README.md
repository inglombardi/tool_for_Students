# tool_for_Students
This tool helps you to compute your AVG BSc or MSc marks but you SHOULD know the Strategy Pattern approach. See my GitHub folder - inglombardi/Test_Automation_Skills

 ________________________________________________________________
 |                  Dott. Ing. Nicola Lombardi                  |
 ================================================================
 |       Author of the Project - Engineer Nicola Lombardi       |
 ================================================================
 | MSc. in Telecommunications and Internet of Things            |
 | Dottore Magistrale | Telecomunicazioni | HW SW ENGINEER      |
 | Trieste, Sgonico, TS - Friuli Venezia Giulia                 |
 |                                                              |
 | Università degli Studi di Cagliari (UniCa, Sardegna, CA)     |
 | Dipartimento di Ingegneria Elettrica ed Elettronica          |
 | Piazza d'Armi, 09123 Cagliari                                |
 ================================================================
 | Linkedin: [Nicola Lombardi]
 (https://it.linkedin.com/in/nicola-lombardi-09046b205) |




===============================================================================================================================================================
|                              # ENGLISH                                                                                                                      |
===============================================================================================================================================================

# Graduation Grade Prediction

### Project Description
This project implements a Python tool to predict graduation grades. Since university regulations can vary significantly between different institutions and faculties, it is impossible to create a perfect, generalizable system. However, by using the **Strategy Pattern**, the tool allows dynamic representation of various regulations, enabling the prediction of a range of graduation grades for any scenario.

While the tool does not explicitly model uncertainties (such as the student's or professor's mood, student preparation, or exam modalities), it provides a practical method to help students organize their academic journey effectively.

---

### Functionality
The code is implemented in Python and uses the following main libraries:
- **FPDF**: To generate a PDF report for each test executed.
- **numpy**: For numerical operations.
- **abc**: To implement abstract classes and the **Strategy Pattern**.
- Other standard libraries such as `random` and `typing`.

**Core Concept**:  
The **Strategy Pattern** was used to dynamically represent different graduation grade calculation methods based on academic regulations. This architecture ensures flexibility and extensibility, making it easy to support new regulations without modifying existing code.

---

### How to Run
#### Prerequisites
- Basic understanding of the **Strategy Pattern** (optional but helpful).
- Python 3.x installed.
- Required libraries: `fpdf`, `numpy`.




===============================================================================================================================================================
|                              # ITALIAN                                                                                                                      |
===============================================================================================================================================================

# Previsione Voto di Laurea

### Descrizione del progetto
Questo progetto implementa un tool in Python per la previsione del voto di laurea. Poiché i regolamenti universitari possono variare significativamente tra diverse Università e Facoltà, non è possibile creare un sistema perfetto e generalizzabile. Tuttavia, utilizzando il **Strategy Pattern**, è possibile rappresentare i diversi regolamenti e predire un range del voto di laurea per ogni situazione.

Il tool tiene conto delle incertezze che influenzano il voto (come lo stato d'animo dello studente o del docente, la preparazione dello studente, e le modalità d'esame), ma non le modella esplicitamente. Lo scopo è aiutare lo studente a pianificare il proprio percorso accademico in modo più organizzato.

---

### Funzionamento
Il codice è implementato in Python e utilizza le seguenti librerie principali:
- **FPDF**: Per generare un report PDF per ogni test eseguito.
- **numpy**: Per operazioni numeriche.
- **abc**: Per implementare classi astratte e il **Strategy Pattern**.
- Altre librerie standard come `random` e `typing`.

**Concetto principale**:  
Il **Strategy Pattern** è stato utilizzato per rappresentare dinamicamente diverse modalità di calcolo del voto di laurea in base ai regolamenti accademici. Questa architettura permette flessibilità ed estensibilità nel supportare nuovi regolamenti senza modificare il codice esistente.

---

### Come eseguirlo
#### Prerequisiti
- Conoscenza del **Strategy Pattern** (opzionale ma utile).
- Python 3.x installato.
- Librerie richieste: 
        import builtins
        import io
        import typing
        from random import random
        import random
        from fpdf import FPDF
        import numpy as np
        from abc import ABC, abstractmethod

Per installare le dipendenze, eseguire:
```bash
pip install fpdf numpy
