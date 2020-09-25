from status_update_validation import status_udpate_validator
from proc_status import Proc_Status
from flask import Flask, render_template, request
application = Flask(__name__)


@application.route('/')
def readme_page():
    return render_template('status_template.j2')


@application.route('/get_proc_statuses')
def simulate_test():
    current_proc_status = Proc_Status()
    return current_proc_status.parse_proc_status()


@application.route('/update_proc_statuses')
def update_proc_status():
    current_proc_status = Proc_Status()
    new_proc_statuses = request.args.get('new_values')
    update_validator = status_udpate_validator(new_proc_statuses)
    validation_results = update_validator.return_validation_results()
    if validation_results == 'All validation checks passed':
        current_proc_status.update_proc_statuses(new_proc_statuses)
        return f'Updated Proc Status File: {current_proc_status.get_proc_status()}'
    else:
        return validation_results


if __name__ == '__main__':
    application.run(host='0.0.0.0')