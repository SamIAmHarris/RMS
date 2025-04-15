# Define static JSON responses
ASSESSMENT_RESPONSE = {
    "assessment": {
        "assessment_id": "1004",
        "focus_id": "stress",
        "preview": {
            "kind": {"assessment": {}},
            "content_id": "1004",
            "focus_id": "stress",
            "duration": 5,
            "units": "minute",
            "title": "Are you sleeping well?",
            "subtitle": "4 questions you can answer to help us guide you to rest well and reduce stress.",
            "template": "default",
            "image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
            "background_color": "#007AFF"
        },
        "options": {
            "reminder": False,
            "skip": True
        },
        "items": [
            {
                "introduction": {
                    "heading": [
                        {
                            "h1": {
                                "text": "Here's the deal.\n10 questions. 5 minutes.\nWith that, we can help you track and improve your mental wellbeing."
                            }
                        }
                    ],
                    "process": [
                        {
                            "h2": {
                                "text": "How it Works"
                            }
                        },
                        {
                            "p": {
                                "text": "This mental wellbeing checkin asks 10 Yes/No questions about your emotions and feels over the past few weeks."
                            }
                        },
                        {
                            "p": {
                                "text": "Questions 1-5 ask about positive emotions you are having. Each Yes response adds one point to your score."
                            }
                        },
                        {
                            "p": {
                                "text": "Questions 6-10 ask about negative feels you might have. Each Yes response subtracts one point from your score."
                            }
                        },
                        {
                            "p": {
                                "text": "Your score will range from +5 to -5. Positive scores indicate a healthy sense of wellbeing. Negative scores indicate you may want to look for opportunities to grow and reach balance."
                            }
                        },
                        {
                            "p": {
                                "text": "Here is a *sample* of the score chart you will see at the end of the checkin:"
                            }
                        },
                        {
                            "img": {
                                "url": "https://refuelapp-dev.web.app/images/bradburn/sample_score.png"
                            }
                        },
                        {
                            "p": {
                                "text": "From time to time, monthly, we'll checkin again on your mental wellbeing with these same questions so we can follow trends on how things are progressing. You will see a chart like this over time as you continue checking in with us."
                            }
                        },
                        {
                            "img": {
                                "url": "https://refuelapp-dev.web.app/images/bradburn/sample_trend.png"
                            }
                        }
                    ],
                    "purpose": [
                        {
                            "h2": {
                                "text": "Why do this? What is the purpose?"
                            }
                        },
                        {
                            "p": {
                                "text": "The checkin is totally voluntary. So, no pressure. Don't do it if you are not comfortable."
                            }
                        },
                        {
                            "p": {
                                "text": "Do this so you can understand if your mental wellbeing is positive or negative and then Refuel can give you better, more focused content in your Today feed that can be helpful to improve yourself in the areas of self-acceptance, building a sense of purpose, creating positive relations with others, and achieveing personal growth. Sound good?"
                            }
                        }
                    ],
                    "privacy": [
                        {
                            "h2": {
                                "text": "Who will see my results?"
                            }
                        },
                        {
                            "p": {
                                "text": "Besides you, your results are shared *anonymously* with your unit commander."
                            }
                        },
                        {
                            "p": {
                                "text": "Before you bail and hit that X in the top left corner, give us a chance to earn your trust. Do the checkin and we'll give you the option at the end to bail and we'll delete all your answers. That's a promise."
                            }
                        },
                        {
                            "p": {
                                "text": "At Project Refuel, we are here to help you and your privacy and trust is important."
                            }
                        }
                    ]
                },
                "fixed": {
                    "item_id": "1",
                    "select": {
                        "min": 1,
                        "max": 6
                    },
                    "prompt": "Over the last 7 days, how do you feel about your sleep?",
                    "responses": [
                        {
                            "response_id": "1",
                            "label": "Tired"
                        },
                        {
                            "response_id": "2",
                            "label": "Well Rested"
                        },
                        {
                            "response_id": "3",
                            "label": "Worn Out"
                        },
                        {
                            "response_id": "4",
                            "label": "Energized"
                        },
                        {
                            "response_id": "5",
                            "label": "Groggy"
                        },
                        {
                            "response_id": "6",
                            "label": "Satisfied"
                        }
                    ]
                }
            },
            {
                "fixed": {
                    "item_id": "2",
                    "select": {
                        "min": 1,
                        "max": 1
                    },
                    "prompt": "On average, how many hours of sleep are you getting each night?",
                    "responses": [
                        {
                            "response_id": "1",
                            "label": "8+"
                        },
                        {
                            "response_id": "2",
                            "label": "5-7"
                        },
                        {
                            "response_id": "3",
                            "label": "3-4"
                        },
                        {
                            "response_id": "4",
                            "label": "1-2"
                        },
                        {
                            "response_id": "5",
                            "label": "None"
                        }
                    ]
                }
            },
            {
                "free": {
                    "item_id": "1001",
                    "prompt": "What things keep you from getting a good night sleep?",
                    "options": {
                        "text": {
                            "characters": {
                                "min": 2,
                                "max": 500
                            }
                        },
                        "audio": {
                            "time": {
                                "max": 60
                            }
                        }
                    }
                }
            },
            {
                "fixed": {
                    "item_id": "1200",
                    "select": {
                        "min": 1,
                        "max": 1
                    },
                    "prompt": "¡We should skip this one!",
                    "responses": [
                        {
                            "response_id": "1",
                            "label": "8+"
                        },
                        {
                            "response_id": "2",
                            "label": "5-7"
                        },
                        {
                            "response_id": "3",
                            "label": "3-4"
                        },
                        {
                            "response_id": "4",
                            "label": "1-2"
                        },
                        {
                            "response_id": "5",
                            "label": "None"
                        }
                    ]
                }
            },
            {
                "scale": {
                    "item_id": "1004",
                    "prompt": "On a scale of 1-5, how would you rate your energy levels?",
                    "min": {
                        "value": 1,
                        "label": "low",
                        "emoji": "😴"
                    },
                    "max": {
                        "value": 5,
                        "label": "high",
                        "emoji": "😀"
                    }
                }
            }
        ]
    }
}

# Action responses
ACTIONS = {
    "next": {"action": {"next": {}}},
    "jump": {"action": {"jump": {"item_id": "-1"}}},
    "mark_completed": {"action": {"mark_completed": {}}},
    "results": {
        "details": {
            "bradburn": {
                "score": -4,
                "trend": [
                    {
                        "label": "Jan",
                        "score": 3
                    },
                    {
                        "label": "Feb",
                        "score": 0
                    },
                    {
                        "label": "Mar",
                        "score": -1
                    },
                    {
                        "label": "Apr",
                        "score": -4
                    }
                ]
            }
        },

        "heading": [
            {
                "h1": {
                    "text": "Your responses indicate a negative psychological wellbeing. That is concerning 😐."
                }
            }
        ],
        "meaning": [
            {
                "h2": {
                    "text": "What does this mean?"
                }
            },
            {
                "p": {
                    "text": "A -4 score means you may be at risk to falling into depression, lowered self esteem, and self-harm."
                }
            },
            {
                "p": {
                    "text": "Your score is not cause for alarm but you may want to look for opportunities and get help building a positive wellbeing improvement plan."
                }
            },
            {
                "button": {
                    "style": "help",
                    "title": "Contact the Psychological Health Resource Center for Help",
                    "url": "https://projectrefuel.app"
                }
            }
        ],
        "scoring": [
            {
                "h2": {
                    "text": "How is the score calculated?"
                }
            },
            {
                "p": {
                    "text": "Questions 1-5 ask about positive emotions you are having. Each Yes adds one point. Questions 6-10 ask about negative emotions you might have. Each Yes response subtracts one point. Scores range from +5 to -5."
                }
            },
            {
                "button": {
                    "style": "normal",
                    "title": "Learn More About",
                    "subtitle": "Refuel Mental Welbeing Checkin",
                    "url": "https://projectrefuel.app"
                }
            }
        ],
        "save": [
            {
                "h2": {
                    "text": "Save your results?"
                }
            },
            {
                "p": {
                    "text": "As promised, we give you the option to save your results. Refuel's AI wellness engine will keep an eye on things and make suggestions to improve your mental wellbeing. Your results will be shared anonymously with your unit leader."
                }
            }
        ]
    }
}

INTRODUCTION_RESPONSE = {
    "heading": [
        {
            "h1": {
                "text": "Here's the deal.\n10 questions. 5 minutes.\nWith that, we can help you track and improve your mental wellbeing."
            }
        }
    ],
    "process": [
        {
            "h2": {
                "text": "How it Works"
            }
        },
        {
            "p": {
                "text": "This mental wellbeing checkin asks 10 Yes/No questions about your emotions and feels over the past few weeks."
            }
        },
        {
            "p": {
                "text": "Questions 1-5 ask about positive emotions you are having. Each Yes response adds one point to your score."
            }
        },
        {
            "p": {
                "text": "Questions 6-10 ask about negative feels you might have. Each Yes response subtracts one point from your score."
            }
        },
        {
            "p": {
                "text": "Your score will range from +5 to -5. Positive scores indicate a healthy sense of wellbeing. Negative scores indicate you may want to look for opportunities to grow and reach balance."
            }
        },
        {
            "p": {
                "text": "Here is a *sample* of the score chart you will see at the end of the checkin:"
            }
        },
        {
            "img": {
                "url": "https://refuelapp-dev.web.app/images/bradburn/sample_score.png"
            }
        },
        {
            "p": {
                "text": "From time to time, monthly, we'll checkin again on your mental wellbeing with these same questions so we can follow trends on how things are progressing. You will see a chart like this over time as you continue checking in with us."
            }
        },
        {
            "img": {
                "url": "https://refuelapp-dev.web.app/images/bradburn/sample_trend.png"
            }
        }
    ],
    "purpose": [
        {
            "h2": {
                "text": "Why do this? What is the purpose?"
            }
        },
        {
            "p": {
                "text": "The checkin is totally voluntary. So, no pressure. Don't do it if you are not comfortable."
            }
        },
        {
            "p": {
                "text": "Do this so you can understand if your mental wellbeing is positive or negative and then Refuel can give you better, more focused content in your Today feed that can be helpful to improve yourself in the areas of self-acceptance, building a sense of purpose, creating positive relations with others, and achieveing personal growth. Sound good?"
            }
        }
    ],
    "privacy": [
        {
            "h2": {
                "text": "Who will see my results?"
            }
        },
        {
            "p": {
                "text": "Besides you, your results are shared *anonymously* with your unit commander."
            }
        },
        {
            "p": {
                "text": "Before you bail and hit that X in the top left corner, give us a chance to earn your trust. Do the checkin and we'll give you the option at the end to bail and we'll delete all your answers. That's a promise."
            }
        },
        {
            "p": {
                "text": "At Project Refuel, we are here to help you and your privacy and trust is important."
            }
        }
    ]
}

EXPLORE_RESPONSE = {
    "explore": {
        "content": [
            {
                "group": {
                    "kind": "checkin",
                    "content": [
                        {
                            "preview": {
                                "duration": 5,
                                "template": "default",
                                "background_color": "#6956B3",
                                "content_id": "8-8404434e116f4ab18f82a1240d559955-07",
                                "units": "minutes",
                                "focus_id": "ideological/spiritual",
                                "image": "https://refuel-backend.d10.us.swri.org/thumbnail_images/spiritual.jpg",
                                "kind": {
                                    "assessment": {
                                        "details": {
                                            "champSSFS": {
                                                "score": 2.764705882352941
                                            }
                                        }
                                    }
                                },
                                "title": "Last time we asked, your spiritual fitness was low. Let's see if things improved."
                            }
                        },
                        {
                            "preview": {
                                "duration": 5,
                                "template": "default",
                                "background_color": "#30B0C7",
                                "content_id": "128-bfd70889edd84353b996dab8ef74378d-07",
                                "units": "minutes",
                                "focus_id": "psychological",
                                "image": "https://refuel-backend.d10.us.swri.org/thumbnail_images/mental-wellbeing.png",
                                "kind": {
                                    "assessment": {
                                        "details": {
                                            "bradburn": {
                                                "score": 2
                                            }
                                        }
                                    }
                                },
                                "title": "It's a good day to ask about your mental wellbeing. Last time, you were feeling positive."
                            }
                        }
                    ]
                }
            },
        ]
    }
}

RESULTS_RESPONSE = ACTIONS["results"]

PFT_TEST_RESPONSE = {
    "test": {
        "id": 1,
        "type": "PFT",
        "description": "PFT description",
        "programmed_exercises": [
            {
                "id": "1",  # exercise table id
                "index": 0,
                "name": "pushups",
                "sets_data": {
                    "prescribed_suffix": "sec",
                    "loggable_suffix": "rep",
                    "items": [
                        {
                            "prescribed_value": 60.0,
                        },
                    ]
                }
            },
            {
                "id": "2",
                "index": 1,
                "name": "situps",
                "sets_data": {
                    "prescribed_suffix": "sec",
                    "loggable_suffix": "rep",
                    "items": [
                        {
                            "prescribed_value": 60.0,
                        },
                    ],
                }
            },
            {
                "id": "3",
                "index": 2,
                "name": "run",
                "sets_data": {
                    "prescribed_suffix": "mi",
                    "loggable_suffix": "pace",
                    "items": [
                        {
                            "prescribed_value": 1.5,
                        }
                    ]
                }
            }
        ],
    }
}
