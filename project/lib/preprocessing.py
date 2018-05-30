import pandas as pd

output_file = 'resources/Interview-processed.xlsx'

sheet_name = 'Dataset'

input_file = 'resources/Interview.xlsx'


class Preprocessing:
    def __init__(self, sheet_name='Dataset', input_file='./resources/Interview.xlsx',
                 output_file='./resources/Interview-processed.xlsx'):
        self.sheet_name = sheet_name
        self.input_file = input_file
        self.output_file = output_file

    def process(self):
        # read file
        data = pd.read_excel(self.input_file, self.sheet_name, index_col=None, na_values=['NA'])
        # select the main model to process
        model = data[
            ['Date', 'Client name', 'Industry', 'Location', 'Position_Type', 'SkillSet_Name',
             'Candidate_ID',
             'Gender', 'Current_Location', 'Company_Location', 'Interview_Venue', 'Candidate_Hometown',
             'Permission_Obtained',
             'No_Unscheduled_Meeting', 'Follow-Up_Call_OK', 'Alternate_Number_Given', 'CV_JD_Ready', 'Venue_Clear',
             'Call_Letter_Received',
             'Expected_Attendance', 'Observed_Attendance', 'Marital_Status'
             ]]

        # Convert categorical variable into dummy/indicator variables
        general_fields = pd.get_dummies(model, columns=['Industry', 'Position_Type',
                                                        'Gender', 'Current_Location', 'Company_Location',
                                                        'Interview_Venue',
                                                        'Candidate_Hometown', 'Permission_Obtained',
                                                        'No_Unscheduled_Meeting', 'Follow-Up_Call_OK',
                                                        'Alternate_Number_Given',
                                                        'CV_JD_Ready', 'Venue_Clear', 'Call_Letter_Received',
                                                        'Expected_Attendance', 'Observed_Attendance', 'Marital_Status'
                                                        ])

        #
        print('Total columns on firts list: {}.'.format(len(general_fields.columns)))


        # split the skill set on different process
        model2 = data[['SkillSet_Name']]
        values = []
        for index, row in model2.iterrows():
            values.append(row[0])

        skillSet_fields = pd.Series(values).str.lower().str.get_dummies(sep="/")

        # merge the skillSet and the general fields
        final_fields = general_fields.merge(skillSet_fields, left_index=True, right_index=True)

        # total columns
        print('Total columns number: {}.'.format(len(final_fields.columns)))


    # Write to output file
        writer = pd.ExcelWriter(self.output_file, engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        final_fields.to_excel(writer, sheet_name=self.sheet_name)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()


if __name__ == '__main__':
    print ("Init...")
    preprocessing = Preprocessing()
    preprocessing.process()
    print ('End...')
