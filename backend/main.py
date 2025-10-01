import os
import json
from fastapi import FastAPI, Request, APIRouter
from pydantic import BaseModel
from langchain_community.llms import Bedrock
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.openapi.toolkit import RequestsToolkit
from langchain_community.utilities.openapi import OpenAPISpec

# --------------------------------------------------
# Globals (will be set on startup)
# --------------------------------------------------
agent = None

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------
app = FastAPI()

# --------------------------------------------------
# Startup: Load OpenAPI spec, Toolkit, LLM, and Agent
# --------------------------------------------------
@app.on_event("startup")
def startup_event():
    global agent
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(BASE_DIR, "wotnot_openapi.json")

        with open(json_path, "r") as f:
            openapi_raw = f.read()

        spec = OpenAPISpec.from_text(openapi_raw)
        spec.base_url = "https://api.wotnot.io"

        toolkit = RequestsToolkit(spec=spec)
        tools = toolkit.get_tools()

        llm = Bedrock(
            model_id="anthropic.claude-v2",
            region_name="us-east-1",
            model_kwargs={"temperature": 0.2}
        )

        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.OPENAI_FUNCTIONS,
            verbose=True
        )
        print("✅ Agent initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")

# --------------------------------------------------
# Bedrock Agent Endpoint
# --------------------------------------------------
@app.post("/run-agent/")
async def run_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "Find content for template, create it, and send to today's contacts.")

    if agent is None:
        return {"error": "Agent not initialized"}

    try:
        result = agent.run(prompt)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}

# --------------------------------------------------
# Message Generator Feature
# --------------------------------------------------
msg_router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

def generate_message(prompt: str) -> str:
    text = prompt.lower()
    if "diwali" in text:
        return "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!"
    elif "new year" in text:
        return "Hello {name}, Happy New Year! Wishing you joy, success, and prosperity!"
    elif "birthday" in text:
        return "Hello {name}, wishing you a wonderful birthday filled with happiness!"
    else:
        return f"Hello {{name}}, {prompt}"

@msg_router.post("/generate-message")
def generate_prompt_message(req: PromptRequest):
    return {"prompt": req.prompt, "message": generate_message(req.prompt)}

# Register new router
app.include_router(msg_router, prefix="/messages", tags=["Message Generator"])
