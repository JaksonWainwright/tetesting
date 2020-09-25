class status_udpate_validator:
    def __init__(self, status):
        self.status = status

    def validate_proc_status_datatype(self):
        try:
            int(self.status)
        except ValueError as e:
            return f'updated_proc_statuses must be integers.'
        except TypeError as e:
            return f'updated_proc_statuses must be integers.'
        else:
            return 'Valid'

    def validate_proc_status_length(self):
        if len(self.status) != 7:
            print(len(self.status))
            return 'updated_proc_statuses must be exactly 7 characters'
        else:
            return 'Valid'

    def validate_proc_status_values(self):
        for value in self.status:
            if value not in ['1', '0']:
                return f'Data is invalid. Must only contain ones or zeros'
        return 'Valid'

    def return_validation_results(self):
        validation_results = [self.validate_proc_status_datatype(), self.validate_proc_status_length(),
                              self.validate_proc_status_values()]
        print(validation_results)
        for item in validation_results:
            if item != 'Valid':
                return item
        return 'All validation checks passed'
