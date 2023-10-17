import os
import json

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Set the OAuth 2.0 credentials.
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(os.path.dirname(__file__), 'credentials.json'),
    'https://www.googleapis.com/auth/forms.body')

# Create the Google Forms API service object.
service = build('forms', 'v1', credentials=credentials)

form = {
    "info": {
        "title": "Operating System Test",
    }
}
result = service.forms().create(body=form).execute()

update = {
    "requests": [
        {
            "updateSettings": {
                "settings": {
                    "quizSettings": {
                        "isQuiz": True
                    }
                },
                "updateMask": "quizSettings.isQuiz"
            }
        }
    ]
}

# Converts the form into a quiz
question_setting = service.forms().batchUpdate(formId=result["formId"],
                                                    body=update).execute()



NEW_QUESTION = {
    "requests":[
  {
    "createItem": {
      "item": {
        "title": "What is the main focus of Accelerate People?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Providing digital IT EPAs"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Providing digital IT EPAs"
                },
                {
                  "value": "Delivering successful digital transformations"
                },
                {
                  "value": "Offering work-readiness programs"
                },
                {
                  "value": "Providing investment management services"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 0
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "Which apprenticeship standards does Accelerate People create End-point Assessments for?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Level 7 Artificial Intelligence (AI) Data Specialist Apprenticeship"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Level 7 Artificial Intelligence (AI) Data Specialist Apprenticeship"
                },
                {
                  "value": "Level 4 Business Analyst Apprenticeship"
                },
                {
                  "value": "Level 4 Cyber Security Technologist Apprenticeship"
                },
                {
                  "value": "Level 3 Digital Marketer Apprenticeship"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 1
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "Which organization commends Agilisys for their dedication and expertise?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "NHSBSA"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "NHSBSA"
                },
                {
                  "value": "Universitas Surabaya"
                },
                {
                  "value": "BCI Capital Limited"
                },
                {
                  "value": "ClearScore"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 2
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What does Avado Learning specialize in?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Work-readiness programs and professional qualifications"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Cloud, IT, and digital transformation services"
                },
                {
                  "value": "Mobile English tests and certificates"
                },
                {
                  "value": "Investment management and advisory services"
                },
                {
                  "value": "Work-readiness programs and professional qualifications"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 3
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What does BCI Capital Limited provide?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Investment management and advisory services"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Digital IT EPAs"
                },
                {
                  "value": "Cloud, IT, and digital transformation services"
                },
                {
                  "value": "Work-readiness programs and professional qualifications"
                },
                {
                  "value": "Investment management and advisory services"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 4
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What does ClearScore offer for free?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Access to credit score and report"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Access to credit score and report"
                },
                {
                  "value": "Work-readiness programs and professional qualifications"
                },
                {
                  "value": "Digital IT EPAs"
                },
                {
                  "value": "Cloud, IT, and digital transformation services"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 5
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What can you identify by regularly checking your credit report?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Signs of fraud"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Signs of fraud"
                },
                {
                  "value": "Discounts on financial products"
                },
                {
                  "value": "Tips for improving your credit score"
                },
                {
                  "value": "Steps to increase your savings"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 6
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "Which category on the ClearScore Support website addresses login issues?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Login issues"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Sign-up problems"
                },
                {
                  "value": "Incorrect credit report sections"
                },
                {
                  "value": "Address-related concerns"
                },
                {
                  "value": "Login issues"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 7
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What does ClearScore provide on their website to help you understand credit scores?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Educational resources"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Educational resources"
                },
                {
                  "value": "Exclusive pre-approved credit offers"
                },
                {
                  "value": "Personalized insights"
                },
                {
                  "value": "Monthly checklists"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 8
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What does Fospha specialize in fixing within 7 days?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Sales attribution"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Credit scores"
                },
                {
                  "value": "Sales attribution"
                },
                {
                  "value": "Customer success"
                },
                {
                  "value": "Accounting errors"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 9
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What is the main focus of Hive Learning's platform?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Peer learning"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Peer learning"
                },
                {
                  "value": "Financial management"
                },
                {
                  "value": "Marketing attribution"
                },
                {
                  "value": "Accounting automation"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 10
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What does Kloo offer as part of their platform for businesses?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Accounts payable automation"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Accounts payable automation"
                },
                {
                  "value": "Credit score monitoring"
                },
                {
                  "value": "Sales attribution analysis"
                },
                {
                  "value": "Peer learning opportunities"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 11
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What is the main focus of Koodoo?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Maximizing the mortgage vertical"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Providing personalized marketing solutions"
                },
                {
                  "value": "Offering embedded business finance solutions"
                },
                {
                  "value": "Transforming lending for the better"
                },
                {
                  "value": "Maximizing the mortgage vertical"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 12
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "How does Liberis utilize Open Banking?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "To expand access to funding for small businesses"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "To streamline the mortgage application process"
                },
                {
                  "value": "To expand access to funding for small businesses"
                },
                {
                  "value": "To detect and prevent financial fraud"
                },
                {
                  "value": "To provide personalized lending solutions"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 13
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What is the product called that Liberis provides?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Business Cash Advance"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Business Cash Advance"
                },
                {
                  "value": "Embedded Business Management"
                },
                {
                  "value": "Open Banking"
                },
                {
                  "value": "Mortgage Monitoring Tools"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 14
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What is the role of AI in detecting and preventing financial fraud?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "To offer scalable and accurate fraud protection"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "To provide personalized lending solutions"
                },
                {
                  "value": "To maximize the mortgage vertical"
                },
                {
                  "value": "To enhance customer targeting"
                },
                {
                  "value": "To offer scalable and accurate fraud protection"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 15
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What is the main focus of Oakbrook?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "Transforming lending for the better"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "Providing personalized marketing solutions"
                },
                {
                  "value": "Offering embedded business finance solutions"
                },
                {
                  "value": "Transforming lending for the better"
                },
                {
                  "value": "Maximizing the mortgage vertical"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 16
      }
    }
  },
  {
    "createItem": {
      "item": {
        "title": "What is the aim of Modulr?",
        "questionItem": {
          "question": {
            "required": True,
            "grading": {
              "pointValue": 1,
              "correctAnswers": {
                "answers": [
                  {
                    "value": "To move money efficiently through businesses"
                  }
                ]
              },
              "whenRight": {
                "text": "You got it!"
              },
              "whenWrong": {
                "text": "Sorry, that's wrong"
              }
            },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [
                {
                  "value": "To maximize the mortgage vertical"
                },
                {
                  "value": "To provide personalized lending solutions"
                },
                {
                  "value": "To automate payments in software"
                },
                {
                  "value": "To move money efficiently through businesses"
                }
              ]
            }
          }
        }
      },
      "location": {
        "index": 17
      }
    }
  }
]
}

# Adds the question to the form
question_setting = service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

# Prints the result to show the question has been added
get_result = service.forms().get(formId=result["formId"]).execute()
print(get_result['responderUri'])