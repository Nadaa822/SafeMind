from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

used = {}

def pick(category, responses):
    if category not in used:
        used[category] = set()

    for r in responses:
        if r not in used[category]:
            used[category].add(r)
            return r

    used[category].clear()
    return random.choice(responses)


def detect(text):
    text = text.lower()

    if any(x in text for x in ["suicide","kill myself","want to die","end my life"]):
        return "crisis"

    if any(x in text for x in ["alone","lonely","no friends"]):
        return "loneliness"

    if any(x in text for x in ["betray","trust","cheated"]):
        return "betrayal"

    if any(x in text for x in ["stress","pressure"]):
        return "stress"

    if any(x in text for x in ["tired","exhausted","drained"]):
        return "burnout"

    if "hopeless" in text:
        return "despair"

    if any(x in text for x in ["anxious","anxiety","overthinking"]):
        return "anxiety"

    return "neutral"


def response(msg):

    t = detect(msg)

    if t == "crisis":
        return (
            "I’m really sorry you're feeling this way. You don’t have to go through this alone.\n\n"
            "Please consider reaching out to someone you trust or a mental health professional. "
            "You can also use the help button below."
        )

    loneliness = [
        "That sounds really isolating… not having someone to talk to can feel heavy.",
        "Do you feel like people are around but not really there for you?",
        "Loneliness can be quiet but painful. When did this start?",
        "Do you feel like you're missing connection or understanding?",
        "Sometimes it’s not about people being there, but feeling seen. Does that relate?",
        "Do you feel emotionally alone or physically alone?",
        "What kind of connection do you wish you had right now?",
        "Do you feel like people don’t really understand you?",
        "Have you felt this way for a long time?",
        "What makes this feeling strongest right now?",
        "If you had someone to talk to, what would you say to them?",
        "Do you feel like you’ve been withdrawing from people?",
        "Sometimes loneliness builds slowly. Has it been like that?",
        "Do you feel like reaching out is hard right now?",
        "Do you feel like you’re being left out or just disconnected?",
        "Is there someone you wish understood you better?",
        "Does it feel like no one really listens?",
        "What’s been making this feeling stronger lately?",
        "Do you feel like you’re going through things alone?",
        "Would it help to talk about what you’ve been holding in?",
    ] * 3

    betrayal = [
        "That sounds really painful… betrayal can break trust deeply.",
        "When someone you trust hurts you, it can stay with you.",
        "Do you feel more hurt or angry right now?",
        "Was this someone close to you?",
        "What part of what happened hurt the most?",
        "Do you keep replaying it in your mind?",
        "Betrayal can make it hard to trust again. Are you feeling that?",
        "Do you feel like things won’t be the same again?",
        "Do you feel like you were treated unfairly?",
        "It’s okay to feel hurt about this. What’s been hardest?",
        "Do you feel like you didn’t expect this from them?",
        "What did this situation take away from you?",
        "Are you finding it hard to move on?",
        "Do you feel like confronting them or avoiding them?",
        "Does it still feel fresh or has it been a while?",
        "Do you feel confused about what happened?",
        "What do you wish had gone differently?",
        "Do you feel like your trust was taken for granted?",
        "Has this changed how you see people?",
        "Would you like to talk through what happened step by step?"
    ] * 3

    stress = [
        "That sounds overwhelming. What’s putting the most pressure on you?",
        "Is this coming from one thing or many things together?",
        "Do you feel like your mind won’t switch off?",
        "What part of this feels hardest to handle?",
        "Have you had any time to rest lately?",
        "Do you feel like expectations are too high?",
        "Are you dealing with this alone?",
        "What’s draining your energy the most?",
        "Do you feel stuck or just overloaded?",
        "Has this been building up over time?",
        "What would help reduce even a small part of this?",
        "Do you feel like you're constantly thinking about it?",
        "Is there anything giving you even a little relief?",
        "Do you feel like you're juggling too many things?",
        "Does it feel urgent or constant?",
        "Have you been able to take breaks?",
        "What’s the most stressful part of this situation?",
        "Do you feel like you’re under pressure from others or yourself?",
        "What usually helps you when things feel like this?",
        "Would it help to break this down into smaller parts?"
    ] * 3

    burnout = [
        "That sounds like deep exhaustion, not just physical tiredness.",
        "Do you feel mentally drained all the time?",
        "Have you been pushing yourself too hard lately?",
        "Do you feel like you're running on autopilot?",
        "When did this exhaustion start?",
        "Do you feel like rest isn’t helping anymore?",
        "Is this coming from work, studies, or everything?",
        "Do you feel like you can’t switch off your mind?",
        "What’s been taking most of your energy?",
        "Have you had any real break recently?",
        "Do you feel emotionally tired too?",
        "Do you feel like you're just getting through the day?",
        "Is it hard to feel motivated?",
        "Do you feel like you’ve been giving too much?",
        "Do you feel like you’re losing interest in things?",
        "What used to energize you that doesn’t anymore?",
        "Do you feel like you’re constantly tired no matter what?",
        "Have you been ignoring your own needs?",
        "Do you feel like you're stretched too thin?",
        "Would slowing down even a little help?"
    ] * 3

    anxiety = [
        "That anxious feeling can be really intense.",
        "Do your thoughts feel hard to control right now?",
        "Is something specific triggering this?",
        "Do you feel restless or uneasy?",
        "Does it come in waves or stay constant?",
        "Do you feel it physically too?",
        "Are you overthinking something repeatedly?",
        "Do you feel like something might go wrong?",
        "Has this been happening often?",
        "What thoughts keep coming back?",
        "Do you feel like you can’t relax?",
        "Do you feel tension in your body?",
        "Is it worse at certain times of day?",
        "What usually helps calm you down?",
        "Do you feel like your mind is racing?",
        "Do you feel overwhelmed by possibilities?",
        "Is it tied to a situation or general?",
        "Do you feel like you need control?",
        "Do you feel stuck in your thoughts?",
        "Would grounding yourself help right now?"
    ] * 3

    despair = [
        "That feeling of hopelessness can be really heavy.",
        "Do you feel like nothing is changing?",
        "What’s been weighing on you the most?",
        "Do you feel stuck or lost?",
        "Has something triggered this recently?",
        "Do you feel like things won’t improve?",
        "What part feels hardest right now?",
        "Do you feel disconnected from your goals?",
        "Is it hard to find motivation?",
        "Do you feel like you're just existing?",
        "Do you feel like things have lost meaning?",
        "What makes it feel especially difficult today?",
        "Do you feel like you're going in circles?",
        "Do you feel like you’ve tried everything?",
        "What’s making it feel this way right now?",
        "Do you feel like you’re running out of energy emotionally?",
        "Do you feel like nothing excites you anymore?",
        "Do you feel like you're losing hope?",
        "What would make things feel slightly better?",
        "Do you feel like you're carrying too much?"
    ] * 3

    neutral = [
        "I’m here to listen. Tell me more.",
        "You can talk freely here.",
        "What’s been on your mind lately?",
        "I’m listening.",
        "Take your time.",
        "What’s been bothering you?",
        "I’m here with you.",
        "Go on, I’m listening.",
        "What’s been happening?",
        "Would you like to share more?",
        "Tell me what’s been going on.",
        "What’s been occupying your thoughts?",
        "I’m here — you don’t have to hold it in.",
        "What’s been affecting you recently?",
        "Feel free to share whatever you’re comfortable with.",
        "What’s been weighing on your mind?",
        "I’m here to understand you.",
        "Take your time, I’m not going anywhere.",
        "What’s been troubling you lately?",
        "Would you like to talk about something specific?"
    ] * 3

    mapping = {
        "loneliness": loneliness,
        "betrayal": betrayal,
        "stress": stress,
        "burnout": burnout,
        "anxiety": anxiety,
        "despair": despair,
        "neutral": neutral
    }

    return pick(t, mapping[t])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]
    return jsonify({"reply": response(msg)})


if __name__ == "__main__":
    app.run(debug=True)