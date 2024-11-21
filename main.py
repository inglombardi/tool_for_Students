import builtins
import io
import typing
from random import random
import random
from fpdf import FPDF
import numpy as np
from abc import ABC, abstractmethod


def print_to_string(*args, **kwargs):
    output = io.StringIO()
    builtins.print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents


# global txt to cast into pdf
f: typing.TextIO = None


def print(*args, **kwargs):
    global f
    f.write(print_to_string(*args, **kwargs))
    return builtins.print(*args, **kwargs)


def export_to_PDF():  # it uses "f" global var
    global f
    if not f:
        return
    f.flush()
    f.seek(0)  # set the pointer to start file (1st byte)
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=6)
    for line in f:
        pdf.cell(200, 10, txt=line, ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("report_global.pdf")
    f.close()


# --- CONTEXT ----

class Student:

    # --------- INIT METHOD -----------------
    def __init__(self, str1=None, str2=None):
        """
         This method builds a Student (Gabriele)
         :param str1: it determines the number of extra points according to the Dissertation date

         Appello_Laurea	Num_punti
                set-24	3
                dic-24	2
                feb-25	1


        :param str2: it determines the number of extra points according to the Dissertation date

         Condizione_Punti_extra_tesi	            Num_punti_(max)
            max 3 pt base inferiore o uguale a 90	3
             3:4 pt base tra 90,001 e 93,999	    4
             4:6 pt superiore 93,999	            6


         :return:
         """
        self.mark_degree = 0
        self.strategy1 = str1
        self.strategy2 = str2

        self.pass_exam_data = {
                'Exam': ['matematica_generale', 'linguaggi', 'matematica_finanziaria', 'macroeconomia',
                          'microeconomia', 'marketing_strategico', 'economia_gestione_imprese',
                          'marketing_operativo', 'tecnica_bancaria'],
                'mark': [21, 30, 18, 23, 20, 26, 28, 22, 26],
                'credits': [12, 8, 6, 9, 12, 9, 9, 6, 9]
        }

        self.NOT_pass_exam_data = {
            'Exam': ['diritto_del_lavoro', 'organizzazione_aziendale', 'statistica', 'economia_aziendale',
                     'ragioneria', 'diritto_commerciale', 'finanza_aziendale',
                     'diritto_privato', 'programmazione_controllo'],
            'mark': [25, 26, 24, 25, 26, 25, 27, 22, 27],
            'credits': [6, 6, 12, 12, 9, 9, 6, 9, 9]
        }

        self.weighted_average_marks = []  # Lista per salvare le medie ponderate
    # getter and setter for attributes ---------------------------------------

    @property
    def mark_degree(self):
        return self._mark_degree

    @property
    def strategy1(self):
        return self._strategy1

    @property
    def strategy2(self):
        return self._strategy2

    @mark_degree.setter
    def mark_degree(self, computed_value):
        self._mark_degree = computed_value

    @strategy1.setter
    def strategy1(self, strategy): # switch of strategy _°\_
        self._strategy1 = strategy

    @strategy2.setter
    def strategy2(self, strategy):  # switch of strategy _°\_
        self._strategy2 = strategy


    # -------------------------------------------------------------------

    @staticmethod
    def weighted_avg(exam_mark_list, exam_credit_list):
        tot_credits = np.sum(exam_credit_list)
        numerator = 0
        for k in range(len(exam_mark_list)):
            numerator += exam_mark_list[k] * exam_credit_list[k]
        return numerator / tot_credits

    @staticmethod
    def converter_into_110_scaling(value):
        return round(value * 110 / 30, 2)

    # attribute modifier (mark_degree)
    def weighted_avg_into_110_scaling(self):
        self.mark_degree = convert_into_110_scaling(weighted_avg(self.pass_exam_data['mark'],self.pass_exam_data['credit']))

    # attribute modifier (weighted_average_marks)
    def calculate_weighted_average(self):
        total_marks = self.pass_exam_data['mark'] + self.NOT_pass_exam_data['mark']
        total_credits = self.pass_exam_data['credits'] + self.NOT_pass_exam_data['credits']


        tot_credits = np.sum(total_credits)
        print("Check -> tot credits : ", tot_credits)
        numerator1 = 0
        num_pass_exam = not_pass_exam = 9
        # compute 1st weighted mean component
        for k in range(num_pass_exam):
            print("======================================================")
            print("Exam -> ", self.pass_exam_data['Exam'][k])
            print("- mark -> ", self.pass_exam_data['mark'][k])
            print("- credit -> ", self.pass_exam_data['credits'][k])
            print(" total_marks[k] -> ", total_marks[k])
            print(" total_credits[k] -> ", total_credits[k], "\n\n")
            numerator1 += total_marks[k] * total_credits[k]

        # compute 2nd weighted mean component
        u = [-3, -2, -1, 0, +1, +2, +3]
        print("\n\n ---- NOT PASSED EXAMS -----\n\n")
        for uj in u:
            numerator2 = 0
            # lower_bound = mark - 3  # Limite inferiore dell'incertezza
            # upper_bound = mark + 3  # Limite superiore dell'incertezza
            k = 0
            for k in range(9):
                print("======================================================")
                print("Exam -> ", self.NOT_pass_exam_data['Exam'][k])
                print("- supposed mark -> ", self.NOT_pass_exam_data['mark'][k])
                print("- credit -> ", self.NOT_pass_exam_data['credits'][k],"\n\n")
                recalibrated = (self.NOT_pass_exam_data['mark'][k] + uj)
                if recalibrated > 30:
                    recalibrated = 30
                elif recalibrated < 18:
                    recalibrated = 18
                numerator2 += recalibrated * self.NOT_pass_exam_data['credits'][k]
                print(" Recalibrated mark -> {} with increase __ {} __".format(recalibrated, uj))

            print("\n\nTot numerator 1 -> ", numerator1)
            print("Tot numerator 2 considering {} of uncertainty -> {}".format(uj,numerator2))
            num_tot_j = numerator1 + numerator2
            print("Check ->  sum between Num1 and Num2 Finished .... {}\n".format(num_tot_j))
            avg_tot_j = round(num_tot_j / tot_credits, 2)
            print(" Check -> total avg considering {} of uncertainty -> {}".format(uj, avg_tot_j))
            starting_mark_j = self.converter_into_110_scaling(avg_tot_j)
            print(" Check -> total mark of degree {} pushed".format(starting_mark_j))
            self.weighted_average_marks.append(starting_mark_j)

    def calculate_weighted_average_random(self):
        total_marks = self.pass_exam_data['mark'] + self.NOT_pass_exam_data['mark']
        total_credits = self.pass_exam_data['credits'] + self.NOT_pass_exam_data['credits']

        tot_credits = np.sum(total_credits)
        print("Check -> tot credits : ", tot_credits)
        numerator1 = 0
        num_pass_exam = not_pass_exam = 9
        # compute 1st weighted mean component
        for k in range(num_pass_exam):
            print("======================================================")
            print("Exam -> ", self.pass_exam_data['Exam'][k])
            print("- mark -> ", self.pass_exam_data['mark'][k])
            print("- credit -> ", self.pass_exam_data['credits'][k])
            print(" total_marks[k] -> ", total_marks[k])
            print(" total_credits[k] -> ", total_credits[k], "\n\n")
            numerator1 += total_marks[k] * total_credits[k]

        # compute 2nd weighted mean component
        # u = [np.random.uniform(-3, 3) for _ in range(not_pass_exam)] # list_comprehension
        u = [random.randint(-3, 3) for _ in range(not_pass_exam)]
        print("\n\n ---- NOT PASSED EXAMS -----\n\n")
        for i, uj in enumerate(u):

            numerator2 = 0
            # lower_bound = mark - 3  # Limite inferiore dell'incertezza
            # upper_bound = mark + 3  # Limite superiore dell'incertezza
            for k in range(not_pass_exam):
                print("======================================================")
                print("Exam -> ", self.NOT_pass_exam_data['Exam'][k])
                print("- supposed mark -> ", self.NOT_pass_exam_data['mark'][k])
                print("- credit -> ", self.NOT_pass_exam_data['credits'][k], "\n\n")
                recalibrated = (self.NOT_pass_exam_data['mark'][k] + uj)
                if recalibrated > 30:
                    recalibrated = 30
                elif recalibrated < 18:
                    recalibrated = 18
                numerator2 += recalibrated * self.NOT_pass_exam_data['credits'][k]
                print(" Recalibrated mark -> {} with increase __ {} __".format(recalibrated, uj))

            print("\n\nTot numerator 1 -> ", numerator1)
            print("Tot numerator 2 considering {} of uncertainty -> {}".format(uj, numerator2))
            num_tot_j = numerator1 + numerator2
            print("Check ->  sum between Num1 and Num2 Finished .... {}\n".format(num_tot_j))
            avg_tot_j = round(num_tot_j / tot_credits, 2)
            print(" Check -> total avg considering {} of uncertainty -> {}".format(uj, avg_tot_j))
            starting_mark_j = self.converter_into_110_scaling(avg_tot_j)
            print(" Check -> total mark of degree {} pushed".format(starting_mark_j))
            self.weighted_average_marks.append(starting_mark_j)

    def acquire_params(self):
        print(" ============== FINAL MARK SECTION ==============")
        print("Choose degree months between: \n 'a' -> september\n 'b' -> december\n 'c' -> february")
        c = str(input("Choose a month : "))
        if c == 'a':
            self.strategy1 = september_Strategy() # strategy dependence
        elif c == 'b':
            self.strategy1 = december_Strategy() # strategy dependence
        elif c == 'c':
            self.strategy1 = february_Strategy() # strategy dependence
        else:
            print("Error Month input ")
            return
        print(" Degree month -> " + str(self.strategy1.__str__()))
        for i in range(len(self.weighted_average_marks)):
            self.weighted_average_marks[i] += self.degree_date()

        for i in range(len(self.weighted_average_marks)):
            if self.weighted_average_marks[i] < 90:
                self.strategy2 = avg_is_lower_90_Strategy()
                g2 = self.degree_thesis() # strategy dependence
                self.weighted_average_marks[i] += g2
            elif 90 < self.weighted_average_marks[i] < 94:
                self.strategy2 = avg_is_between_90_94_Strategy()
                g2 = self.degree_thesis()  # strategy dependence
                self.weighted_average_marks[i] += g2
            else:
                self.strategy2 = avg_is_upper_94_Strategy()
                g2 = self.degree_thesis()  # strategy dependence
                self.weighted_average_marks[i] += g2
        print("All scenarios : \n ", self.weighted_average_marks)


    def input_controlled_process(self):
        #self.calculate_weighted_average()
        self.calculate_weighted_average_random()
        self.acquire_params()

    # --------------- method for strategy 1
    def degree_date(self):
        # strategy is set up in the main
        gain1 = self.strategy1.increase_degree_date()
        return gain1

    # --------------- method for strategy 2
    def degree_thesis(self):
        # strategy is set up in the main
        gain2 = self.strategy2.increase_degree_thesis()
        return gain2



# ------------------ END CONTEXT ----------------------


#--------- STRATEGIES IMPLEMENTATION  ( --- 1 ---)


class Strategy1(ABC):
    @abstractmethod
    def increase_degree_date(self):
        pass

class september_Strategy(Strategy1):
    def increase_degree_date(self):
        return 3

class december_Strategy(Strategy1):
    def increase_degree_date(self):
        return 2

class february_Strategy(Strategy1):
    def increase_degree_date(self):
        return 1

#--------- STRATEGIES IMPLEMENTATION  ( --- 2 ---)
class Strategy2(ABC):
    @abstractmethod
    def increase_degree_thesis(self):
        pass
class avg_is_lower_90_Strategy(Strategy2):
    def increase_degree_thesis(self):
        return 3
class avg_is_between_90_94_Strategy(Strategy2):
    def increase_degree_thesis(self):
        return 4
class avg_is_upper_94_Strategy(Strategy2):
    def increase_degree_thesis(self):
        return 6






def weighted_avg(exam_mark_list, exam_credit_list):
    tot_credits = np.sum(exam_credit_list)
    numerator = 0
    for k in range(len(exam_mark_list)):
        numerator += exam_mark_list[k] * exam_credit_list[k]
    return numerator/tot_credits

def union_data(pass_dict, not_pass_dict):
    # Unire i due dizionari
    merged_data = {
        'Exam': pass_dict['Exam'] + not_pass_dict['Exam'],
        'mark': pass_dict['mark'] + not_pass_dict['mark'],
        'credits': pass_dict['credits'] + not_pass_dict['credits']
    }
    return merged_data

def convert_into_110_scaling(value):
    return round( value*110/30, 2)


def uncert_weighted_avg(total_exam_mark_list, total_exam_credit_list):
    tot_credits = np.sum(total_exam_credit_list)
    numerator1 = numerator2 = 0
    num_pass_exam = not_pass_exam = 9
    u = [-3,-2,-1,0,+1,+2,+3]

    for k in range(num_pass_exam):
        numerator1 += total_exam_mark_list[k] * total_exam_credit_list[k]

    for uj in u:
        for k in range(num_pass_exam, num_pass_exam + not_pass_exam):
            numerator2 += ( total_exam_mark_list[k] + uj ) * total_exam_credit_list[k]

        num_tot = numerator1 + numerator2
        print("Check ->  sum between Num1 and Num2 Finished .... \n")
        avg_tot = round( num_tot / tot_credits, 2)
        print(" Check -> total avg considering {} of uncertainty")
        starting_mark = convert_into_110_scaling(avg_tot)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    f = open("output.txt", "w+")  # Open the file for writing
    print("\n\t\t Gabriele's Degree possible marks\n\n")
    print("---------------- degree mark SOLUTION: STRATEGY PATTERN APPROACH -----------------------")
    print(" ___________ Rules :")
    print(" _________")
    print("Appello_Laurea	Num_punti")
    print("set-24	               3pt.")
    print(" dic-24	               2pt.")
    print(" feb-25	               1pt.")
    print(" _________")
    print("     Condizione_Punti_extra_tesi	            Num_punti_(valori massimi) ")
    print("max 3 pt base inferiore o uguale a 90	           3pt.")
    print("3:4 pt base tra 90,001 e 93,999	                   4pt.")
    print("4:6 pt superiore 93,999	                           6pt.")
    print(" _________")

    # Definisci il dataset di esami passati
    pass_exam_data = {
        'Exam': ['matematica_generale', 'linguaggi', 'matematica_finanziaria', 'macroeconomia',
                  'microeconomia', 'marketing_strategico', 'economia_gestione_imprese',
                  'marketing_operativo', 'tecnica_bancaria'],
        'mark': [21, 30, 18, 23, 20, 26, 28, 22, 26],
        'credits': [12, 8, 6, 9, 12, 9, 9, 6, 9]
    }

    NOT_pass_exam_data = {
        'Exam': ['diritto_del_lavoro', 'organizzazione_aziendale', 'statistica', 'economia_aziendale',
                 'ragioneria', 'diritto_commerciale', 'finanza_aziendale',
                 'diritto_privato', 'programmazione_controllo'],
        'mark': [25, 26, 24, 25, 26, 25, 27, 22, 27],
        'credits': [6, 6, 12, 12, 9, 9, 6, 9, 9]
    }
    print(" =================== test section for avg computation ===========================")
    # test :
    avg_Gabriele = weighted_avg(pass_exam_data['mark'],pass_exam_data['credits'])
    print("The actual Gabriele's avg is: ", avg_Gabriele)
    rounded_avg_Gabriele = round(weighted_avg(pass_exam_data['mark'],pass_exam_data['credits']),2)
    print("The actual Gabriele's avg ROUNDED is: ", rounded_avg_Gabriele)
    print("The current __ starting pass mark __ for Degree is -> ", round(avg_Gabriele*110/30, 2) )
    print(" Thesis is NOT INCLUDED IN THIS EVALUATION ")
    tot_dict = union_data(pass_exam_data,NOT_pass_exam_data)
    #print(tot_dict)
    print(" =================== end test section ===========================\n\n\n\n\n")




    print("Passed exams : \n ", pass_exam_data['Exam'],"\n")
    print("Assumptions : \n ", NOT_pass_exam_data['Exam'],"\n",NOT_pass_exam_data['mark'])
    # DATE TIME -> strategy 1
    # the client must declare three strategy object
    sep_strategy = september_Strategy()
    dec_strategy = december_Strategy()
    feb_strategy = february_Strategy()

    # THESIS EVALUATION -> strategy 2
    lower_strategy = avg_is_lower_90_Strategy()
    between_strategy = avg_is_between_90_94_Strategy()
    upper_strategy = avg_is_upper_94_Strategy()


    g = Student()
    g.input_controlled_process()


    # Call export_to_PDF after writing the content to the file
    export_to_PDF()

