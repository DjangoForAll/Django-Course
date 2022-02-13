We’ll be following the [agile methodology](https://www.atlassian.com/agile/project-management) to develop our application. User Stories in agile methodology refers to an informal and general explanation of a software feature written from the perspective of the end-user. Its purpose is to articulate how a software feature will provide value to the customer.

Before we jump onto the user stories in this system, here are the main entities you would be dealing with.

- Facility: It can be a PHC or CHC.
- Patient: In our system, a patient is an object whose data we are dealing with, and they never get to use the software. A patient is registered in a PHC and is only referred to a CHC.

## User Stories

### District Admin

This persona will have the most access in the system and has eyes everywhere. They will be in control of all the facilities(PHC or CHC) and their specialists in a given district.

Here is how they will interact with the system:

- Manage facilities:  
  Admin will maintain a list of facilities and all their relevant data. Remember every facility belongs to a ward but not every ward has a facility. Every patient also belongs to a ward but can be registered in any facility. Filtering and sorting should also be doable. Only facilities can be soft-deleted and updated.
- Registering and managing nurses:  
  Since this system has to be secure and allow only verified nurses to access the critical health records of patients, the admin will be responsible for filling out forms with the details of the nurses to be onboarded. An onboarding email will be sent to the respective nurses. Filtering and sorting the nurses should also be doable. Nurse records should have a soft-delete option.
- Assign nurses to facilities:  
  Only the admin has the power to assign nurses (primary or secondary) to each facility. This can be done while registering.

  > Every nurse must be assigned to a facility.

  When a primary or secondary nurse logins to the system for the first time, they will be required to set a password for themselves and should only be able to login with an email that the admin entered while registering their profile on the system.

### Primary Nurse

This user persona is responsible for maintaining all the health records for a particular patient under their PHC.

Here is how they will interact with the system:

- Manage list of patients:  
  Filtering and sorting the patients should be doable.
- CRUD operations on patient object:  
  A nurse can register a patient with their personal details to the facility the former belongs to and update the below categories during the first visit. Provision for sending an email with the treatment summary report consisting of all the data collected about the patient should be done. Patient records should have a soft-delete option.

  A patient object has 4 major categories:

  - Personal Details
  - Family Details
  - Health Information
  - Treatment history

- Visit the patient:  
  During a visit, a primary nurse will be adding health information, will be viewing the active treatments and adding notes for each active treatment in that particular visit. The nurse will also be able to refer the patient to any secondary nurse in the district especially based on their skillset (treatments they specialise in) from the patient dashboard. They can always view the patient dashboard and make edits to the first 2 categories above.

  Brownie Points: Filter the secondary nurses in the ward to which the PHC of the primary nurse belongs to.

- Schedule a visit:  
  A nurse has to deal with a lot in a day. To make their lives easier, we want to enable them with a feature that allows them to prioritise their visits to critical patients on a daily basis.
  They should have a daily agenda view like in any digital calendar which they can reschedule and cross off their visits as they go about their day.

### Secondary Nurse

This user persona belongs only to a CHC and is the specialist nurse that provides special care for a patient only when referred by a primary nurse.
They have equal access to all data and interact with the system exactly like a primary nurse.

The only difference is that they deal with patients being referred to them. They can see all data including all the patient objects under their CHC.

### Common Features

- All users will have the option to change their passwords.
- Nurses can update their personal information by requesting the district admin. ( For Brownie Points )

### Background Jobs

- Daily Report  
  Nurses will be sent an email every day at a configurable time with the daily report of their work, number of patients handled, treatments they did etc. for bookkeeping.
- Patient Report  
  After a patient's data is updated, their treatment summary should be sent to their relative ( can be stored on the patient model ).

### Dependent Filters

In the application the attribute `ward` is used in multiple occasions, there might be thousands of ward in the system and finding the right one can be a time consuming task, loading all the wards at the same time can be computationally expensive as well, to mitigate such issues we can use dependent filters which first ask for a state, which then shows the districts filtered by the state, then the LSG's filtered by the district and then the ward filtered by the LSG. This makes the process of selecting a ward extremely simple and intuitive for the user, in the backend we avoid fetching all the wards as well.

This approach is hard to implement with server side rendering alone since the HTML content changes based on the user's selection, This feature can be implemented with basic API's and javascript, This feature is not a requirement for this capstone but I highly reccomend building this feature to understand basic javascript and an API flow.

Read the following [document](https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html) for more info on buildin the javascript part
