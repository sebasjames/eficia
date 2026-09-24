import{cl as u}from"./vendor-D_8A8kPZ.js";const m=`
Eres "Avalon AI", un asistente experto en análisis de datos corporativos y gestión comercial.
RESPONDE SIEMPRE EN ESPAÑOL.

Reglas ESTRICTAS:
1. Basa tus respuestas EXCLUSIVAMENTE en el JSON de contexto proporcionado (incluyendo los metadatos y resúmenes).
2. Si el usuario pregunta por cantidades (ej. "¿Cuántos productos hay?"), SIEMPRE lee el nodo "resumen" (summary) del JSON y usa esos números exactos. NUNCA intentes contar los elementos del array manualmente.
3. Si un dato no está presente en el JSON, responde honestamente que no tienes esa información. ¡NO INVENTES DATOS (Cero alucinaciones)!
4. Sé conciso, profesional y basado puramente en la realidad de la información entregada. Usa viñetas cuando sea apropiado para listar información.
5. No menciones que estás leyendo un JSON, simplemente responde con naturalidad como si tuvieras acceso directo a la base de datos de la empresa.
`,d=()=>localStorage.getItem("gemini_api_key"),N=async(a,t=null)=>{try{const e=d();if(!e)return"Error: No se ha configurado la API Key de Avalon AI > Scarpian AI. Por favor, ingresa tu clave de producto en el módulo de configuración o ingesta.";const o=new u({apiKey:e}),r=`
        [CONTEXTO DE DATOS DEL SISTEMA (EN TIEMPO REAL)]:
        ${t?JSON.stringify(t):"No hay datos de contexto adicionales proporcionados."}
        
        [CONSULTA DEL USUARIO]:
        ${a}
        `;return(await o.models.generateContent({model:"gemini-3.5-flash",contents:r,config:{systemInstruction:m}})).text||"Procesé los datos pero no pude generar una respuesta textual."}catch(e){return console.error("Gemini API Error:",e),"Hubo un error al procesar tu solicitud con Gemini. Revisa la consola para más detalles."}},y=async a=>{const t=()=>a.map(e=>{const o=e.totalStock*.4+100,s=Math.ceil(Math.max(0,o*3-e.totalStock));let r="Stock estable";return e.totalStock<o?r="Riesgo de quiebre en < 30 días":e.totalStock<o*2&&(r="Stock de seguridad bajo (sugerido 3 meses)"),{sku:e.sku,description:e.name,currentStock:e.totalStock,unitCost:e.unitCost,suggestedQty:s,reason:r,editedQty:s}});try{const e=d();if(!e)return console.warn("Using local fallback for purchase suggestions (No API Key)."),t();const o=new u({apiKey:e}),s=`
        Analiza este subconjunto del inventario de Inruzz Jeans:
        ${JSON.stringify(a.map(n=>({sku:n.sku,name:n.name,stock:n.totalStock,cost:n.unitCost})))}
        
        Genera una sugerencia de pedido para asegurar inventario de confección y fardos para los próximos 3 meses, asumiendo un consumo mensual moderado y tiempos de reposición de 30 días.
        
        RESPONDE ÚNICAMENTE CON UN ARRAY JSON. NADA DE MARKDOWN, NADA DE TEXTO ADICIONAL.
        Estructura requerida por elemento:
        { "sku": "str", "description": "str", "currentStock": num, "unitCost": num, "suggestedQty": num, "reason": "str", "editedQty": num (igual a suggestedQty) }
        `,i=((await o.models.generateContent({model:"gemini-3.5-flash",contents:s,config:{systemInstruction:"Eres un asistente de compras de Inruzz Jeans. Responde SOLO con el array JSON solicitado, sin comillas invertidas ni bloques de código markdown.",temperature:.1}})).text||"").replace(/```json/gi,"").replace(/```/gi,"").trim(),c=JSON.parse(i);return Array.isArray(c)?c:t()}catch(e){return console.error("Error in generatePurchaseSuggestions:",e),t()}},E=async(a,t)=>{try{const e=d();if(!e)return console.warn("No API key, returning mock AI suggestion"),a.map(n=>{const l=n.quantity||n.qty||n.totalUnits||100;return{sku:n.sku,splits:[{location:"Bogotá (San Victorino)",qty:Math.floor(l*.7)||1},{location:"Medellín (Guayaquil)",qty:l-(Math.floor(l*.7)||1)}].filter(g=>g.qty>0),justification:"Sugerencia de prueba: Se asignó 70% a Bogotá San Victorino por alta demanda mayorista."}});const o=new u({apiKey:e}),s=`
Eres el módulo de IA Logística de Inruzz Jeans. 
Se acaba de recibir un lote de mercancía textil / fardos (Inventario en Tránsito). Tu objetivo es decidir a qué bodegas y puntos de venta (Bogotá San Victorino, Medellín Guayaquil, Cali) enviar cada fracción de los productos para balancear el stock.

INVENTARIO ACTUAL EN PUNTOS PARA ESTOS SKUS:
${JSON.stringify(t,null,2)}

MERCANCÍA RECIBIDA (EN TRÁNSITO):
${JSON.stringify(a,null,2)}

Devuelve estrictamente un arreglo JSON (sin markdown, sin bloques de código) con el siguiente formato:
[
  {
    "sku": "SKU-DEL-PRODUCTO",
    "splits": [
       { "location": "NombreBodega", "qty": CantidadNumerica }
    ],
    "justification": "Explicación breve de por qué se tomó esta decisión (ej. 'Bogotá San Victorino tiene rotación rápida de fardos, se envía el 70% allí.')."
  }
]
IMPORTANTE: La suma de 'qty' en 'splits' DEBE ser exactamente igual a la cantidad total del producto recibido.
Solo puedes usar las bodegas: Bogotá (San Victorino), Medellín (Guayaquil), Cali.
`,i=((await o.models.generateContent({model:"gemini-3.5-flash",contents:s,config:{systemInstruction:"Eres un experto en inventario. Responde ÚNICAMENTE con el arreglo JSON solicitado. No agregues texto adicional ni markdown."}})).text||"[]").replace(/```json/g,"").replace(/```/g,"").trim();return JSON.parse(i)}catch(e){return console.error("Gemini API Error (Auto-Distribution):",e),[]}};export{y as a,N as g,E as s};
