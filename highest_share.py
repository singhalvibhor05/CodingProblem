"""
Problem:
Consider Share prices for a N number of companies given for each month since year
1990 in a CSV file.  Format of the file is as below with first line as header.

Year,Month,Company A, Company B,Company C, .............Company N
1990, Jan, 10, 15, 20, , ..........,50
1990, Feb, 10, 15, 20, , ..........,50
.
.
.
.
2013, Sep, 50, 10, 15............500

List for each Company year and month in which the share price was highest.
Sample csv file is share in the repo.
"""
import csv


def is_valid_csv_headers(headers):
    """
    methods to validate the headers of the file.
    input: headers
    output true/false
    """
    if len(headers) <= 2:
        return False
    if not (headers[0].lower() == 'year' and headers[1].lower() == 'month'):
        return False
    return True


def get_max_shares_list(csv_file):
    """
    read the passed csv file and return the companies year and month in which
    the share price was highest.
    """
    try:
        f = open(csv_file, 'rb')
        reader = csv.reader(f)
        headers = reader.next()

    except IOError:
        return False, 'CSV file does not exist, check file path or put csv '\
                       'file in same folder and give absolute path'
    except Exception as e:
        return False, str(e)
    else:
        if not is_valid_csv_headers(headers):
            err_msg = 'Invalid csv'
            return False, err_msg
        # file has been validated now.
        rec_dict = {}
        company_list = headers[2:]

        for record in reader:
            year, month = record[:2]
            shares = map(int, record[2:])
            for company, share in zip(company_list, shares):
                if company not in rec_dict or rec_dict[company][2] < share:
                    rec_dict[company] = [year, month, share]

        return True, rec_dict



# code to run the file as script.
#if __name__ == '__main__':
#    csv_file = raw_input('Enter csv file path: ')
#
#    status, data = get_max_shares_list(csv_file)
#
#    if status:
#        for company, record in data.iteritems():
#            print company, record
#    else:
#
#        print data
