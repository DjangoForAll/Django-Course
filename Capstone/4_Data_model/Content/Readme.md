# Database models
#### state
This model may only have a `name`.

#### district
This model can have a `name` and will be related to a `state`.

#### lsg body
This model should contain:

- `name`
- `kind`: an LSG can be of different types like Gram Panchayat, Municipality, etc.
- `lsg_body_code`: unique code of the lsg body. refer to the [care repo](https://github.com/coronasafe/care/blob/master/care/users/models.py#L61)

and will be related to a `district`.

#### ward
This model should contain:

- `name`,
- `number`: number associated with the ward,

and should be related to a `lsg_body`
#### facility
This model should contain

- `kind`: a facility may be a PHC or a CHC,
- `name`,
- `address`,
- `pincode`,
- `phone`,

and should be related to a `ward`.

#### user
This model can be used as a base for multiple types of users: `primary_nurse`, `secondary_nurse`, `district_admin`.

This can contain the basic information that would be common to all the users:

- `full name`,
- `role`: The role of the user,
- `email`,
- `phone`,
- `is_verified`: the verification status of the user,
- `password`: for users to login,

and should be related to a `district`, `facility`. Use the User model that django provides, do not create a new model altogether.
#### patient
This model should contain all the basic necessary details of a patient:

- `full_name`,
- `date_of_birth`,
- `address`,
- `landmark`,
- `phone`,
- `gender`,
- `emergency_phone_number`,
- `expired_time`: if they have expired,
- `ward`

and should be related to a `facility`.
#### family detail
This model should contain the family member’s details of a patient. This should have:

- `full_name`,
- `phone`,
- `date_of_birth`,
- `email`,
- `relation`: how is this member related to the patient (dropdown),
- `address`,
- `education`,
- `occupation`,
- `remarks`,
- `is_primary`: a family member can be set as primary

and should be related to a `patient`.

#### disease
This model can have:

- `name`: name of the disease
- `icds_code`: International Classification of Diseases code

For sample data, please refer to [this](https://github.com/coronasafe/arike/blob/main/db/seeds/development/diseases.seeds.rb)

#### patient disease
This model should connect a patient with disease(s) and each should contain a `note` field that can describe the condition further.
#### visit schedule
- `date` and `time` of the schedule
- `duration`

and it should be related to a patient and a user (nurse)
#### visit details
- `palliative_phase`
- `blood_pressure`
- `pulse`
- `General_Random_Blood_Sugar `
- `Personal_hygiene`
- `Mouth_hygiene`
- `Pubic_hygiene`
- `systemic_examination`
- `patient_at_peace`: is the patient at peace?
- `pain`: does the patient feel pain?
- `symptoms`: could be multiple (multi-select)
- `note`: special notes for the visit

It should be related to a `visit schedule`

#### treatment
- `description`: description of the treatment,
- `care_type`: type of care,
- `care_sub_type`: sub-type of the care,

for care types and subtypes, refer to [this](https://github.com/coronasafe/arike/blob/main/db/seeds/development/treatment.seeds.rb)

It should be related to a `patient`

#### treatment_notes
- `note` - notes for the treatment
- `description`: description of the treatment,
- `care_type`: type of care,
- `care_sub_type`: sub-type of the care,

it should be related to every `visit` and `treatment`

> Note: each model should maintain a `created_at` and `updated_at` properties. There should only be soft deletion! No record should be permanently deleted.
> You are free to name the attributes however you want as long it follows database attribute naming conventions and makes sense.
