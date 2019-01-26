# /api/users/{id}

```
{
    "id": 1,
    "name": "Kim",
    "email": "fake@email.com",
    "gender": "nonbinary",
    "memberships": [
        "YWCA": {
            "preferred_locations": [
                "Uptown",
                "Downtown",
                "Midtown"
            ]
        },
        "YMCA": {
            "preferred_locations": [
            ]
        }
    ],
    "preferred_days": [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ],
    "preferred_times": [
        "Early morning",
        "Late morning",
        "Afternoon",
        "Evening",
        "Night",
        "Late night"
    ],
    "preferred_genders": [
        "male",
        "female",
        "nonbinary"
    ],
    "preferred_workouts": [
        "cardio",
        "strength",
        "team sports",
        "group classes"
    ]
}
```

# /api/users/{query_string}

* Can add query string for `preferred_days`
* Can add query string for `preferred_genders`
* Can add query string for `preferred_times`
* Can add query string for `preferred_workouts`
* Can add query string for `memberships`

# /api/workouts

```
{
    "workouts": [
        "cardio",
        "strength",
        "team sports",
        "group classes"
    ]
}
```

# /api/days

```
{
    "days": [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]
}
```

# /api/times

```
{
    "times": [
        "Early morning",
        "Late morning",
        "Afternoon",
        "Evening",
        "Night",
        "Late night"
    ]
}
```
