Follow this checklist to ensure that your project is ready for submission.

## District Admin

### Manage facilities

- Create
- View
- Edit
- Delete
- List
- Filtering according to ward and kind ( Brownie Points for Dependent Filters )
- Sorting according to any relevant parameters. ( Created/Modified Time ) ( Brownie Points )
- Search

### Registering and managing nurses/users

- Create
- View
- Update
- Delete
- List
- Filtering according to role and facility assigned
- Sorting according to any relevant parameters. ( Brownie Points )
- Search
- Assign facility and role to a given nurse
- Onboarding email sent once the user is created ( Temp password is okay for MVP )

## Primary Nurse

### Login

- Set password during first-time login

### Manage list of patients

- Create
- View patient dashboard
- Edit patient personal details, Assigning Nurse ( Brownie Points: Filter the nurse by their skill)
- Delete
- List
- Filtering according to ward and facility ( Brownie Points for Dependent Filters )
- Sorting according to any relevant parameters. ( Brownie Points )
- Search
- Assigning CHC Nurses

### Patient Dashboard

- Visit history and details view
- Family Details CRUD
- Disease history CRUD
- Treatments CRUD

### Schedule a visit

- List of patients with filter and sort
- Search patient
- Create
- Agenda with date selection ( Brownie Points )

### During a Visit

- Health info form with relevant details
- View active treatments and their notes
- Add treatment notes

## Secondary Nurse

- Same features as a primary nurse to be checked for.
- Patients appear in their schedule visit list only when assigned to them
- badge to indicate that they have been assigned to a patient from a PHC ( Brownie Points )

## Common Features

- Profile page with the option to change their passwords. ( Brownie Points )
- Home dashboard

## Background Jobs

### Daily Report

- Nurses will be sent an email every day at a configurable time with the daily report of their work, the number of patients handled, treatments they did, etc. for bookkeeping.
  
### Patient Report

- After a patient's data is updated, their treatment summary should be sent to their relatives ( emails can be stored in the family members model ).
