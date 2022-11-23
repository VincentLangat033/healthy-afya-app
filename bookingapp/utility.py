def appointment_availability(schedule_data):
    available = []
    for schedule in schedule_data:
        if schedule == 'monday' and schedule_data[schedule] == 'Available':
            available.append(1)
        elif schedule == 'tuesday' and schedule_data[schedule] == 'Available':
            available.append(2)
        elif schedule == 'wednesday' and schedule_data[schedule] == 'Available':
            available.append(3)
        elif schedule == 'thursday' and schedule_data[schedule] == 'Available':
            available.append(4)
        elif schedule == 'friday' and schedule_data[schedule] == 'Available':
            available.append(5)
        elif schedule == 'saturday' and schedule_data[schedule] == 'Available':
            available.append(6)
        elif schedule == 'sunday' and schedule_data[schedule] == 'Available':
            available.append(0)
    return available
