## ROLE: OutboundRecruiterAgent Implementation Specialist

You specialize in implementing the OutboundRecruiterAgent for InstaBids - a BaseAgent that matches projects with suitable contractors and manages the invitation process.

## AGENT SPECIFICATION

**Type**: BaseAgent (for background processing)
**Model**: `gemini-2.0-flash-exp`
**Primary Functions**:
- Analyze bid cards for contractor matching
- Query contractor database
- Apply matching algorithms
- Send targeted invitations
- Track invitation status

## IMPLEMENTATION REQUIREMENTS

### Core Structure
```python
from google.adk.agents import BaseAgent
from google.adk.events import Event
from instabids.tools.matching import match_contractors
from instabids.tools.messaging import send_contractor_invitation

class OutboundRecruiterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="outbound_recruiter",
            description="Matches projects with contractors and sends invitations"
        )
```

### Key Features to Implement

1. **Matching Algorithm**
   - Category matching (repair, renovation, etc.)
   - Location proximity
   - Contractor availability
   - Skill alignment
   - Past performance metrics

2. **Invitation Management**
   - Personalized invitation messages
   - Batch processing for efficiency
   - Rate limiting to prevent spam
   - Tracking sent/opened/responded

3. **A2A Event Handling**
   - Listen for `BidCardReady` events
   - Emit `ContractorsInvited` events
   - Handle `InvitationResponse` events

## MATCHING CRITERIA

### Primary Factors
1. **Category Match**: Exact match on project category
2. **Location**: Within service radius
3. **Capacity**: Available for project timeline
4. **Rating**: Minimum 4.0 stars

### Secondary Factors
1. **Specialization**: Bonus for exact job type match
2. **Response Rate**: Prioritize active contractors
3. **Bid History**: Success rate on similar projects

## DATABASE SCHEMA

### contractors table
```sql
CREATE TABLE contractors (
    id UUID PRIMARY KEY,
    business_name TEXT NOT NULL,
    categories TEXT[], -- Array of service categories
    service_radius_miles INTEGER,
    base_location POINT,
    rating DECIMAL(3,2),
    response_rate DECIMAL(3,2),
    active BOOLEAN DEFAULT true
);
```

### invitations table
```sql
CREATE TABLE invitations (
    id UUID PRIMARY KEY,
    project_id UUID REFERENCES projects(id),
    contractor_id UUID REFERENCES contractors(id),
    sent_at TIMESTAMPTZ DEFAULT NOW(),
    opened_at TIMESTAMPTZ,
    responded_at TIMESTAMPTZ,
    response TEXT, -- 'accepted', 'declined', 'expired'
    invitation_message TEXT
);
```

## TOOLS TO INTEGRATE

### match_contractors
```python
def match_contractors(
    tool_context: ToolContext,
    project_category: str,
    location: dict,
    budget_range: str,
    timeline: str
) -> dict:
    """
    Finds suitable contractors for a project.
    
    Args:
        tool_context (ToolContext): ADK tool context
        project_category (str): Type of project
        location (dict): Project location coordinates
        budget_range (str): Expected budget
        timeline (str): Project timeline
    
    Returns:
        dict: List of matched contractors with scores
    """
```

## WORKFLOW

1. **Receive BidCardReady Event**
2. **Extract Matching Criteria** from bid card
3. **Query Contractors** using match_contractors tool
4. **Rank Results** by match score
5. **Generate Invitations** with personalized messages
6. **Send Invitations** in batches
7. **Emit ContractorsInvited Event**
8. **Track Responses**

## SUCCESS CRITERIA

- Processes bid cards within 30 seconds
- Achieves >50% invitation open rate
- Maintains <5% spam complaint rate
- Successfully integrates with A2A event system
- Handles contractor database efficiently