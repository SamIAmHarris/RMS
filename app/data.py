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
        "action": {
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
                "slot_id": 0,
                "options": [
                    {
                        "exercise_id": "1",
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
                        "exercise_id": "2",
                        "name": "hand release pushups",
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
                ],
            }, {
                "slot_id": "2",
                "options": [
                    {
                        "exercise_id": "3",
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
                        "exercise_id": "4",
                        "name": "cross leg reverse crunch",
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
                        "exercise_id": "5",
                        "name": "plank hold",
                        "sets_data": {
                            "prescribed_suffix": "sec",
                            "loggable_suffix": "sec",
                            "items": [
                                {
                                    "prescribed_value": 60.0,
                                },
                            ],
                        }
                    },
                ]
            },
            {
                "slot_id": "3",
                "options": [
                    {
                        "exercise_id": "6",
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
                    },
                    {
                        "exercise_id": "7",
                        "name": "hamr",
                        "sets_data": {
                            "prescribed_suffix": "sec",
                            "loggable_suffix": "reps",
                            "items": [
                                {
                                    "prescribed_value": 20,
                                },
                            ]
                        }
                    },
                    {
                        "exercise_id": "8",
                        "name": "walk",
                        "sets_data": {
                            "prescribed_suffix": "k",
                            "loggable_suffix": "pace",
                            "items": [
                                {
                                    "prescribed_value": 2.0,
                                }
                            ]
                        }
                    },
                ]
            }
        ],
    }
}

PFT_LOGGED_RESPONSE = {
    "exercise_id": "1",
    "notes": "I CRUSHED THIS. I AM GOKU",
    "logged_sets_data": [
        {
            "set_number": 0,
            "logged_value": 38,
            "logged_suffix": "rep",
            "notes": "Really hard for me, I need to work on my pushups."
        },
        {
            "set_number": 1,
            "logged_value": 52,
            "logged_suffix": "rep"
        },
        {
            "set_number": 2,
            "logged_value": 11.4,
            "logged_suffix": "pace"
        }
    ]
}

VERTICAL_PAGE_RESPONSE = {
    "vertical_page": {
        "vertical_page_id": "1004",
        "focus_id": "stress",
        "title": "Training vs Instinct",
        "header_image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
        "preview": {
            "kind": {"vertical_page": {}},
            "content_id": "1004",
            "focus_id": "stress",
            "duration": 5,
            "units": "minute",
            "title": "Training vs Instinct",
            "subtitle": "Let's work through an interactive scenario to practice...",
            "template": "default",
            "image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
            "background_color": "#007AFF"
        },
        "options": {
            "skip": True
        },
        "items": [
            {
                "section": {
                    "item_id": "12345",
                    "markdown": "all markdown passed down in whole, instead of it all chunked out.",
                    "sections": [
                        {
                            "h1": {
                                "text": "When Protocol Meets The Unknown"
                            },
                        },
                        {
                            "p": {
                                "text": "Standard Operating Procedures (SOPs) are built on repetition. They're forged through hard-earned lessons, codified into protocols that can be trained, drilled, and relied on. In high-stakes environments, they act like muscle memory—speeding up decisions when there's no time to hesitate.  But what happens when the moment doesn’t look like the drill? When the person in front of you isn’t behaving like the pattern you’ve trained for? In these moments, something else kicks in. "
                            },
                        },
                        {
                            "img": {
                                "url": "https://refuelapp-dev.web.app/images/bradburn/sample_score.png"
                            }
                        },
                        {
                            "q": {
                                "text": "I am a quote by a wise wise owl"
                            }
                        },
                        {
                            "box": {
                                "text": "I am boxed in, nothing going outside the box"
                            }
                        },
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

CONSUME_PAGE_RESPONSE = {
    "consume_page": {
        "consume_page_id": "mock-001",
        "focus_id": "resilience",
        "title_full": "The Edge of Adaptation: an Activity Helping You Understand Who Knows What",
        "title_short": "The Edge of Adaptation",
        "title_image": "https://images.unsplash.com/photo-1519074031893-210d39bd3885?crop=entropy&cs=tinysrgb&[…]JjZXxlbnwwfHx8fDE3NDY2NjIwMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
        "preview": {
            "kind": {
                "consume_page": {}
            },
            "content_id": "mock-001",
            "focus_id": "resilience",
            "duration": 7,
            "units": "minute",
            "title": "The Edge of Adaptation",
            "subtitle": "Explore how you adapt under pressure.",
            "template": "default",
            "image": "https://images.unsplash.com/photo-1519074031893-210d39bd3885?crop=entropy&cs=tinysrgb&[…]JjZXxlbnwwfHx8fDE3NDY2NjIwMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
            "background_color": "#0055FF"
        },
        "progress": {
            "section_id": "s2"
        },
        "sections": [
            {
                "item_id": "s1",
                "markdown": "## Section 1: Pressure Points\n\n**Understanding Your Default Reaction to Stress**\n\n> _\"The pressure you feel is not from the situation itself, but from your perception of it.\"_\n\nWhen the unexpected hits, how do you react? Some go calm and quiet. Others leap into action. And a few... simply freeze. These responses aren't right or wrong—they're clues to how you process change.\n\n---\n\n### \ud83d\udd0d What Pressure Can Reveal\n- **Fight**: Charging into action, sometimes prematurely\n- **Flight**: Avoiding or deflecting responsibility\n- **Freeze**: Stalled, overwhelmed by possibilities\n- **Flow**: Calm, aware, and navigating intentionally\n\n#### \ud83d\udcac Real Talk\n> *\"When I was put on the spot last week, I panicked at first... but then remembered to breathe.\"* — anonymous contributor\n\n---\n\n### \ud83e\udde9 Exploration Prompts\n1. Recall the last high-pressure moment.\n2. What physical sensations did you notice?\n3. Did you lean on logic or instinct?\n4. How did others perceive your response?\n\n---\n\n### \ud83d\udca1 Tip Box\n**Practice makes presence.**  \nRehearsing scenarios mentally can make your future responses more fluid.\n\n---\n\n### \ud83d\udd9a Wrapping Up\nKnowing your pressure response helps you reframe it. Next time you're tested—observe. Don't judge. Awareness is the beginning of resilience.",
                "inputs": [
                    {
                        "type": "fixed",
                        "item_id": "q1",
                        "skippable": False,
                        "prompt": "How do you typically respond to unexpected challenges?",
                        "subtitle": "Select one option",
                        "select": {
                            "min": 1,
                            "max": 1
                        },
                        "responses": [
                            {
                                "response_id": "1",
                                "label": "Stay calm and assess",
                                "subtitle": "keep it calm",
                                "preview_text": "A steady mindset can be powerful."
                            },
                            {
                                "response_id": "2",
                                "label": "React immediately",
                                "subtitle": "quick quick",
                                "preview_text": "Quick thinking has its advantages."
                            },
                            {
                                "response_id": "3",
                                "label": "Panic and freeze",
                                "subtitle": "panic time",
                                "preview_text": "Recognizing this is the first step to improvement."
                            }
                        ]
                    },
                    {
                        "type": "scale",
                        "item_id": "q2",
                        "skippable": True,
                        "prompt": "On a scale from 1–5, how in control do you feel in high-stress situations?",
                        "subtitle": "Choose a place on the scale",
                        "min": {
                            "value": 1,
                            "label": "Out of control",
                            "emoji": "😰"
                        },
                        "max": {
                            "value": 5,
                            "label": "Completely in control",
                            "emoji": "💪"
                        },
                        "preview_text": [
                            "preview text 1",
                            "preview text 2",
                            "preview text 3",
                            "preview text 4",
                            "preview text 5"
                        ]
                    }
                ]
            },
            {
                "item_id": "s2",
                "markdown": "## Section 2: Inside the Storm\n\n**The Chaos Within: Can You Stay Centered?**\n\n> _\"Storms make trees take deeper roots.\"_ — Dolly Parton\n\nThis section is about learning to adapt when your environment spins out of control. Think of it as mental jiu-jitsu: not resisting force, but using it.\n\n---\n\n### \ud83c\udf2a\ufe0f What Storms Teach Us\n- **Chaos is natural**: Plans unravel.\n- **Discomfort is data**: Stress reveals blindspots.\n- **Adaptation is a skill**: Not a gift, but a learned response.\n- **Awareness is a choice**: You can choose to observe instead of react.\n- **Grounding techniques work**: They center you, fast.\n\n---\n\n### \ud83d\udd0d Deep Dive: Types of Adaptive Thinking\n#### \ud83e\udde0 Reactive Thinkers\n- Solve immediate problems\n- Quick on their feet, but may overlook details\n- Prone to snap decisions\n- Often excellent in crises, but need follow-up\n\n#### \ud83d\udcad Reflective Thinkers\n- Pause and evaluate\n- May appear slow, but often get to better outcomes\n- Use hindsight and foresight together\n- Especially good in long-term planning\n\n---\n\n### \ud83c\udf27\ufe0f Mental Weather Report\n- Identify today’s dominant emotion\n- Forecast how it might evolve\n- Prepare a mental umbrella (support, tools, mindset)\n\n---\n\n### \ud83d\udccc Exercises to Try\n- **Write** about a recent pivot point.\n- **Visualize** your internal ‘weather map’. Is it stormy or clear?\n- **Breathe** in for 4, hold for 4, out for 6. Repeat until grounded.\n- **Speak aloud** your current state without judgment.\n- **Stand up** and stretch. Physical movement helps emotional clarity.\n\n---\n\n> *\"Adaptability is not about knowing what will happen. It's about being ready to respond when it does.\"*\n\n---\n\n### \ud83e\uddf0 Coping Toolbox\n- \ud83c\udfc3 Exercise\n- \ud83e\uddd8 Meditation\n- \ud83d\udc64 Talking it out\n- \ud83c\udfae Healthy distractions\n- \ud83d\udcdd Journaling your responses\n- \ud83c\udf0a Time in nature\n- \ud83d\udcfa Silence/low stimulation\n\n---\n\n### \ud83d\udea8 Bonus Challenge\nReframe the next stressor that hits you: Instead of\"Why is this happening to me?\"Try\"What is this teaching me?\"\n\nReflect, ground, adapt. You’ve got this.",
                "inputs": [
                    {
                        "type": "free",
                        "item_id": "q3",
                        "skippable": False,
                        "prompt": "Describe a time when you had to quickly adjust to new information.",
                        "subtitle": "Let it rip",
                        "options": {
                            "text": {
                                "characters": {
                                    "min": 10,
                                    "max": 500
                                }
                            },
                            "audio": {
                                "time": {
                                    "max": 60
                                }
                            }
                        }
                    },
                    {
                        "type": "fixed",
                        "item_id": "q4",
                        "skippable": True,
                        "prompt": "Which of the following have helped you cope with stress recently? (Select all that apply)",
                        "subtitle": "Select as many as you'd like",
                        "select": {
                            "min": 0,
                            "max": 4
                        },
                        "responses": [
                            {
                                "response_id": "1",
                                "label": "Exercise",
                                "subtitle": "keep it calm",
                                "preview_text": "sweat it out"
                            },
                            {
                                "response_id": "2",
                                "label": "Talking to someone",
                                "subtitle": "keep it talkative",
                                "preview_text": "talk it out"
                            },
                            {
                                "response_id": "3",
                                "label": "Meditation",
                                "subtitle": "keep it breathable",
                                "preview_text": "breathe it out"
                            },
                            {
                                "response_id": "4",
                                "label": "Distraction (TV, games, etc.)",
                                "subtitle": "keep it distractable",
                                "preview_text": "distract it out"
                            }
                        ]
                    }
                ]
            },
            {
                "item_id": "s3",
                "markdown": "## Section 3: Reflective Space\n\n**Inner Compass: Where Are You Pointing?**\n\nClarity isn’t a luxury—it’s a necessity.\n\nWhat matters now?\n\nThink briefly. Move forward mindfully.",
                "inputs": [
                    {
                        "type": "scale",
                        "item_id": "q5",
                        "skippable": False,
                        "prompt": "How much clarity do you feel about your current priorities?",
                        "subtitle": "Choose an option on the scale",
                        "min": {
                            "value": 1,
                            "label": "Not clear",
                            "emoji": "🤷"
                        },
                        "max": {
                            "value": 5,
                            "label": "Crystal clear",
                            "emoji": "🔍"
                        },
                        "preview_text": [
                            "preview text 1",
                            "preview text 2",
                            "preview text 3",
                            "preview text 4",
                            "preview text 5"
                        ]
                    }
                ]
            },
            {
                "item_id": "s4",
                "markdown": "## Section 4: Final Thought\n\n**The Pressure Reset Button**\n\n> _\u201cBetween the stimulus and the response, there is a space...\u201d_ — Viktor Frankl\n\nYou've explored how you respond to pressure. You've identified coping tools and reflected on clarity. Now: what's one thing you'll do differently?\n\n---\n\n### \ud83c\udf1f Reset Goals\n**What do you want to change?**\n- Less reactivity, more intention?\n- Deeper breath before responding?\n- Healthier self-talk?\n\n---\n\n### \ud83d\uddfd Create a North Star Phrase\n> *\"In pressure, I choose... [calm/clarity/focus/strength]\"*\n\nWrite your own mantra and repeat it next time your blood pressure spikes.\n\n---\n\n### \ud83d\udd04 Loop it Forward\n#### Next time you feel pressure:\n1. Pause for 5 seconds.\n2. Notice where tension lives in your body.\n3. Recall this activity—and your growth.\n\n---\n\n### \ud83e\udd28 Bonus Exercise\n#### \u201cMy New Response Plan\u201d\n- When pressure hits, I will...\n- I will remind myself that...\n- I’ll reach out to...\n\n---\n\n### \ud83d\udcac Final Prompt\n> *\"When pressure builds, I want to become the kind of person who...\"*\n\n---\n\n### \ud83d\udca1 Remember\n**Growth doesn’t happen at the edge of ease. It happens at the edge of adaptation.**  \nThank you for walking to that edge today.",
                "inputs": [
                    {
                        "type": "free",
                        "item_id": "q6",
                        "skippable": True,
                        "prompt": "What would you like to change about how you handle pressure?",
                        "subtitle": "Let it rip",
                        "options": {
                            "text": {
                                "characters": {
                                    "min": 5,
                                    "max": 300
                                }
                            },
                            "audio": {
                                "time": {
                                    "max": 45
                                }
                            }
                        }
                    }
                ]
            }
        ]
    }
}

TODAY_PAGE_RESPONSE = {
    "today": {
        "date": "2025-05-28",
        "greeting": {
            "text": "Let’s end your day strong, Josh.",
            "supporting_text": "You’ve been sticking to your afternoon routine — nice work. Keep it up!"
        },
        "top_content": [
            {
                "preview": {
                    "kind": {
                        "assessment": {
                            "assessment": {
                                "assessment_id": "2000",
                                "resume_item_id": "2",
                                "items": [
                                    {
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
                                        "scale": {
                                            "item_id": "1004",
                                            "prompt": "On a scale of 1–5, how would you rate your energy levels?",
                                            "min": {
                                                "value": 1,
                                                "label": "normal",
                                                "emoji": "😀"
                                            },
                                            "max": {
                                                "value": 5,
                                                "label": "low",
                                                "emoji": "😴"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    "content_id": "1004",
                    "duration": 5,
                    "units": "minute",
                    "template": "story_card_inline",
                    "title": "Let's end your day strong, Josh.",
                    "subtitle": "You've been sticking to your afternoon routine - nice work. Keep it up!",
                    "image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
                    "background_color": "#007AFF",
                    "cta": ""
                }
            },
            {
                "preview": {
                    "kind": {
                        "assessment": {
                            "assessment": {
                                "assessment_id": "2001",
                                "items": [
                                    {
                                        "fixed": {
                                            "item_id": "10",
                                            "select": {
                                                "min": 1,
                                                "max": 1
                                            },
                                            "prompt": "Have you taken time to relax today?",
                                            "responses": [
                                                {
                                                    "response_id": "1",
                                                    "label": "Yes"
                                                },
                                                {
                                                    "response_id": "2",
                                                    "label": "No"
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "scale": {
                                            "item_id": "11",
                                            "prompt": "Rate today's stress (1–5)",
                                            "min": {
                                                "value": 1,
                                                "label": "Calm",
                                                "emoji": "🧘"
                                            },
                                            "max": {
                                                "value": 5,
                                                "label": "Stressed",
                                                "emoji": "😫"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    "content_id": "1005",
                    "duration": 3,
                    "units": "minute",
                    "template": "story_card_inline",
                    "title": "End your day Strong:",
                    "subtitle": "Before the day ends, take a moment to recognize something you did well -- big or small.",
                    "image": "",
                    "cta": "",
                    "background_color": ""
                }
            },
            {
                "preview": {
                    "kind": {
                        "assessment": {}
                    },
                    "content_id": "1006",
                    "duration": 5,
                    "units": "minute",
                    "template": "story_card",
                    "title": "How was your workout yesterday?",
                    "subtitle": "Give us some feedback in order to get better insights for the week.",
                    "image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
                    "background_color": "#007AFF",
                    "cta": "Start Check-in"
                }
            },
            {
                "preview": {
                    "kind": {
                        "journal": {}
                    },
                    "content_id": "1010",
                    "duration": 2,
                    "template": "story_card",
                    "units": "minute",
                    "title": "Journal today, you are on a 4 day streak, keep up the good work.",
                    "subtitle": "Start a chat here...",
                    "cta": "Start a conversation here...",
                    "image": "",
                    "background_color": "#FFEEDD"
                }
            }
        ],
        "bottom_content": [
            {
                "title": "Morning Routine",
                "subtitle": "Start with focus and calm",
                "section_id": "0",
                "expanded": True,
                "icon": "https://api.iconify.design/mdi/pen.svg",
                "progress_label": "1 of 3",
                "items": [
                    {
                        "template": "task_item_expanded",
                        "status": "late",
                        "bookmarked": False,
                        "priority": True,
                        "source": "goal",
                        "index": 0,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3001",
                            "duration": 3,
                            "units": "minute",
                            "title": "Morning Momentum",
                            "subtitle": "How to prime your mindset before the day begins",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#FFF3E0"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "index": 1,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3002",
                            "duration": 2,
                            "units": "minute",
                            "title": "Drink Water First",
                            "subtitle": "Rehydration boosts focus and mood.",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E0F7FA"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "index": 2,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3003",
                            "duration": 1,
                            "units": "minute",
                            "title": "Stretch and Wake Up",
                            "subtitle": "Gentle morning movement to open the day",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#FFFDE7"
                        }
                    }
                ]
            },
            {
                "title": "Midday Reset",
                "subtitle": "Boost energy and intention",
                "section_id": "1",
                "expanded": False,
                "icon": "https://api.iconify.design/mdi/box.svg",
                "progress_label": "1 of 3",
                "items": [
                    {
                        "template": "task_item",
                        "status": "in_progress",
                        "index": 0,
                        "bookmarked": False,
                        "priority": False,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3101",
                            "duration": 4,
                            "units": "minute",
                            "title": "Take a Breath Break",
                            "subtitle": "",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E8F5E9"
                        }
                    },
                    {
                        "template": "task_item_expanded",
                        "status": "completed",
                        "bookmarked": False,
                        "priority": False,
                        "source": "goal",
                        "index": 1,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3102",
                            "duration": 3,
                            "units": "minute",
                            "title": "Midday Movement",
                            "subtitle": "Gentle stretch or walk to reenergize yourself before you head out to do that thing. And remember that we need to also see if you can and yes that is good to know.",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E0F2F1"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "in_progress",
                        "bookmarked": False,
                        "priority": False,
                        "index": 2,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3103",
                            "duration": 2,
                            "units": "minute",
                            "title": "Mindful Moment",
                            "subtitle": "A two-minute mental reset for clarity",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#FFF8E1"
                        }
                    }
                ]
            },
            {
                "title": "Evening Wind-Down",
                "subtitle": "Reflect and recharge",
                "section_id": "2",
                "expanded": True,
                "icon": "https://api.iconify.design/mdi/cloud.svg",
                "progress_label": "0 of 3",
                "items": [
                    {
                        "template": "task_item_expanded",
                        "status": "complete",
                        "bookmarked": True,
                        "priority": False,
                        "source": "goal",
                        "index": 0,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3201",
                            "duration": 5,
                            "units": "minute",
                            "title": "Sleep Prep: Unplug",
                            "subtitle": "Digital detox tips for better sleep",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E3F2FD"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "late",
                        "bookmarked": False,
                        "priority": False,
                        "index": 1,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3202",
                            "duration": 3,
                            "units": "minute",
                            "title": "Evening Gratitude",
                            "subtitle": "Reflect on something good from your day",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#F3E5F5"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "index": 2,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3203",
                            "duration": 2,
                            "units": "minute",
                            "title": "Read Something Inspiring",
                            "subtitle": "Wind down with uplifting thoughts",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#F1F8E9"
                        }
                    }
                ]
            }
        ]
    }
}

REFRESH_TODAY_PAGE_RESPONSE = {
    "today": {
        "date": "2025-05-28",
        "greeting": {
            "text": "Here are some new tasks for you Josh!.",
            "supporting_text": "Let's get after it today, you got some new work ready!"
        },
        "top_content": [
            {
                "preview": {
                    "kind": {
                        "assessment": {
                            "assessment": {
                                "assessment_id": "2000",
                                "items": [
                                    {
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
                                        "scale": {
                                            "item_id": "1004",
                                            "prompt": "On a scale of 1–5, how would you rate your energy levels?",
                                            "min": {
                                                "value": 1,
                                                "label": "normal",
                                                "emoji": "😀"
                                            },
                                            "max": {
                                                "value": 5,
                                                "label": "low",
                                                "emoji": "😴"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    "content_id": "1004",
                    "duration": 5,
                    "units": "minute",
                    "template": "story_card_inline",
                    "title": "You’re Wrapping Up Strong.",
                    "subtitle": "Great job keeping your momentum today",
                    "image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
                    "background_color": "#007AFF",
                    "cta": ""
                }
            },
            {
                "preview": {
                    "kind": {
                        "assessment": {
                            "assessment": {
                                "assessment_id": "2001",
                                "items": [
                                    {
                                        "fixed": {
                                            "item_id": "10",
                                            "select": {
                                                "min": 1,
                                                "max": 1
                                            },
                                            "prompt": "Have you taken time to relax today?",
                                            "responses": [
                                                {
                                                    "response_id": "1",
                                                    "label": "Yes"
                                                },
                                                {
                                                    "response_id": "2",
                                                    "label": "No"
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "scale": {
                                            "item_id": "11",
                                            "prompt": "Rate today's stress (1–5)",
                                            "min": {
                                                "value": 1,
                                                "label": "Calm",
                                                "emoji": "🧘"
                                            },
                                            "max": {
                                                "value": 5,
                                                "label": "Stressed",
                                                "emoji": "😫"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    "content_id": "1005",
                    "duration": 3,
                    "units": "minute",
                    "template": "story_card_inline",
                    "title": "Finish on a High Note",
                    "subtitle": "Celebrate your wins before winding down",
                    "image": "",
                    "cta": "",
                    "background_color": ""
                }
            },
            {
                "preview": {
                    "kind": {
                        "assessment": {}
                    },
                    "content_id": "1006",
                    "duration": 5,
                    "units": "minute",
                    "template": "story_card",
                    "title": "Reflect on Your Workout",
                    "subtitle": "Your feedback helps shape your progress",
                    "image": "https://refuelapp-dev.web.app/content/1004/images/preview.png",
                    "background_color": "#007AFF",
                    "cta": "Give Feedback"
                }
            },
            {
                "preview": {
                    "kind": {
                        "journal": {}
                    },
                    "content_id": "1010",
                    "duration": 2,
                    "template": "story_card",
                    "units": "minute",
                    "title": "Keep the Streak Going",
                    "subtitle": "You’re on a roll — keep journaling daily",
                    "cta": "Open Journal",
                    "image": "",
                    "background_color": "#FFEEDD"
                }
            }
        ],
        "bottom_content": [
            {
                "title": "Morning Kickstart",
                "subtitle": "Fuel your day with energy and purpose",
                "section_id": "0",
                "expanded": True,
                "icon": "https://api.iconify.design/mdi/pen.svg",
                "progress_label": "1 of 3",
                "items": [
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "index": 0,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3401",
                            "duration": 7,
                            "units": "minute",
                            "title": "Rise and Shine",
                            "subtitle": "Energize your mind before the hustle starts",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#FFF3E0"
                        }
                    },
                    {
                        "template": "task_item_expanded",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "source": "goal",
                        "index": 1,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3402",
                            "duration": 22,
                            "units": "minute",
                            "title": "Hydration Hero",
                            "subtitle": "Power up with a glass of water. And think about doing the one thing that needs to be done before the other things and who knows why it is called a oh yes I get it.",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E0F7FA"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": True,
                        "index": 2,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3403",
                            "duration": 4,
                            "units": "minute",
                            "title": "Wake-Up Warmup",
                            "subtitle": "",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#FFFDE7"
                        }
                    }
                ]
            },
            {
                "title": "Lunchtime Recharge",
                "subtitle": "Restore clarity and presence",
                "section_id": "1",
                "expanded": False,
                "icon": "https://api.iconify.design/mdi/box.svg",
                "progress_label": "1 of 3",
                "items": [
                    {
                        "template": "task_item_expanded",
                        "status": "incomplete",
                        "index": 0,
                        "bookmarked": False,
                        "priority": False,
                        "source": "goal",
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3501",
                            "duration": 5,
                            "units": "minute",
                            "title": "Deep Breath Reset",
                            "subtitle": "Slow breathing to reset and refocus",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E8F5E9"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "index": 1,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3502",
                            "duration": 31,
                            "units": "minute",
                            "title": "Power Pause Movement",
                            "subtitle": "Move a little, boost a lot",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E0F2F1"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "index": 2,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3503",
                            "duration": 12,
                            "units": "minute",
                            "title": "Mental Refresh",
                            "subtitle": "Clear your mind in just two minutes",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#FFF8E1"
                        }
                    }
                ]
            },
            {
                "title": "Evening Cool Down",
                "subtitle": "Unwind and get ready for tomorrow",
                "section_id": "2",
                "expanded": True,
                "icon": "https://api.iconify.design/mdi/cloud.svg",
                "progress_label": "0 of 3",
                "items": [
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": True,
                        "priority": False,
                        "index": 0,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3601",
                            "duration": 1,
                            "units": "minute",
                            "title": "Unplug and Unwind",
                            "subtitle": "Disconnect to rest better",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#E3F2FD"
                        }
                    },
                    {
                        "template": "task_item_expanded",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": False,
                        "source": "goal",
                        "index": 1,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3602",
                            "duration": 4,
                            "units": "minute",
                            "title": "Day-End Thanks",
                            "subtitle": "Appreciate what today brought",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#F3E5F5"
                        }
                    },
                    {
                        "template": "task_item",
                        "status": "incomplete",
                        "bookmarked": False,
                        "priority": True,
                        "index": 2,
                        "preview": {
                            "kind": {
                                "consume_page": {}
                            },
                            "content_id": "3603",
                            "duration": 5,
                            "units": "minute",
                            "title": "Inspiration Read",
                            "subtitle": "Close your day on a positive note",
                            "image": "https://api.iconify.design/mdi/home.svg",
                            "background_color": "#F1F8E9"
                        }
                    }
                ]
            }
        ]
    }
}

ACTIVATE_PAGE_RESPONSE = {
    "activate_page_id": "101",
    "domain": {
        "name": "Emotional Resilience",
        "icon": "https://api.iconify.design/mdi/home.svg"
    },
    "header": {
        "image": "https://images.unsplash.com/photo-1540539234-c14a20fb7c7b?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "icon": "https://api.iconify.design/mdi/home.svg",
        "tagline": "Decide with Less Stress",
        "headline": "You don't need the perfect answer. You need a calm one.",
        "introduction": "Overthinking steals time, drains energy, and rarely leads to better outcomes. Today we'll practice shifting from what if to what's next -- with tools that quiet mental clutter and help you move forward.",
        "recommendation_reason": "This was recommended based on your goal to build stronger decision-making under uncertainty.",
    },
    "input_card" : {
        "answered": False,
    },
    "activities" : [
        {
            "activity_id": "201",
            "title": "Shrink the Stakes",
            "image": "",
            "description": "User the 5-5-5- rule to shift perspective from the moment to the other moment and yes that is interesting."
        }
    ],
    "learn_more": [
        {"text" : "1. Learn more about Emotional Resilience"},
        {"text" : "2. Learn more about Emotional Resilience"},
        {"text" : "3. Learn more about Emotional Resilience"},
        {"text" : "4. Learn more about Emotional Resilience"},
    ],
    "instruction_block": {
        "title": "Select an activity and return later",
    },
    "motivation_card": {
        "quote": "Never be in a hurry; do everything quietly and in a calm spirit. Do not lose your inner peace for anything whatsoever, even if your whole world seems upset. - Saint Francis de Sales"
    }
}

ACTIVITY_RESPONSE = {
    "activity_id": "201",
    "why_text": "Why this? Based on your recent check-in and focus on Emotional Resilience",
    "header": {
        "title": "Shrink the Stakes",
        "icon": "https://api.iconify.design/mdi/home.svg",
        "tagline": "Use throughout the day",
        "image": "https://images.unsplash.com/photo-1476055090065-a605fefd840e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fGFjdGl2aXR5fGVufDB8fDB8fHww",
    },
    "conversation_prompt": {
        "prompt": "Ask yourself: Will this decision matter in 5 minutes? 5 days? 5 years?",
        "supporting_text": "This quick mental model helps reduce emotional intensity and unlock clarity. Most daily decisions don't need existential weight -- just forward movement."
    },
    "instructions": [

    ],
    "when_text": "When you're stuck, spinning, or anxious about making the 'perfect' choice.",
    "history": [],
    "reflection": {
        "button_text": "Mark as Done",
    },
    "motivation_card": "Life doesn’t get easier or more forgiving, we get stronger and more resilient. - Steve Maraboli",
}
