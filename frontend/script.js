async function evaluate(){

const question =
document.getElementById("question").value;

const answer =
document.getElementById("answer").value;

const response =
await fetch(
'http://localhost:8000/evaluate',
{
method:'POST',
headers:{
'Content-Type':'application/json'
},
body:JSON.stringify({
question,
answer
})
});

const data =
await response.json();

let html = `
<h2>Total Score:
${data.total_score}
</h2>
`;

data.concept_scores.forEach(c=>{

html += `
<div class="card">

<h3>${c.concept}</h3>

<p>
Score:
${c.score}
</p>

<p>
Similarity:
${c.similarity}
</p>

<p>
${c.feedback}
</p>

</div>
`;

});

document.getElementById(
'result'
).innerHTML = html;

}
