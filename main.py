import discord 
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event 
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command() 
async def hola(ctx): 
    await ctx.send(f'Hola, soy un bot, y te voy a ayudar a disminuir el uso de plastico en tu día a día. Si quieres saber como disminuir el uso de este material, escribe "uno". Si quieres saber como afecta el plastico a nuestro planeta, escribe "dos". Si quieres saber como el uso plástico puede llegar a afectarnos escribe "tres".')

@bot.command() 
async def uno(ctx): 
    await ctx.send(f'Hay muchas diferentes maneras de disminuir el uso del plastico en tu día a día: ') 
    await ctx.send(f'1. Por ejemplo, a veces, cuando tenemos sed, lo primero que pensamos es en comprar una botella de plastico. Esto, ademas de ser dañino, puede ser evitado. Si todos empezamos a llevar nuestra propia botella a todas partes, no solo nos ahorraremos una gran cantidada de dinero, si no que tambien estaremos salvando de alguna u otra manera a muchos animales.') 
    await ctx.send(f'2. Otra opcion es simple mente evitar comprar cosas de este material. Ahora, auque esta tarea pueda ser algo dificil, no es necesario parar por completo la compra d este material. Sin embrgo, podemos para de comprarlo para cosas inecesarias. Algunos ejemplos son lo vasos, platos, y cubiertos de plastico.') 
    await ctx.send(f'3. La tercera opcion es usar el plastico que usas a diario para hacer manualidades. Esto ademas de ser divertido puede ser muy eficiente! Ya que al hacer una maceta, o algo asi, no solo te entretienes, si no que tambien puedes ayudar a limpiar un muy pequeño porcentaje de aire! ')

@bot.command() 
async def dos(ctx): 
    await ctx.send(f'Estas son algunas de las maneras en las que el plastico afecta a nuestro planeta:') 
    await ctx.send(f'1. EL plástico no se degrada facilmente. Puede tardar cientos o miles de años en decomponerse, acumulándose en ríos, oceanos, suelos y paisajes naturales. Con el tiempo este se fragmentará en partículas muy pequeñas llamadas microplásticos, que termina en el agua, el aire y hasta en los alimentos que consumimos.') 
    await ctx.send(f'2. Muchas especies (tortugas, aves, peces, etc.) confunden el plástico con comida y lo ingieren. Esto puede causar asfixia, bloqueos intestinales y muerte. Otros animales pueden quedar atrapados en redes, bolsas o anillos de plástico, esto les impide moverse o alimentase.') 
    await ctx.send(f'3. La fabricación de plástico utiliza combustibles fósiles, lo que genera emisiones de efecto invernadero. Cuendo el plástico se quema con basura, libera gases y contribuye al calentamiento global.') 
    await ctx.send(f'4. En muchos lugares, el plástico no se recicla correctamente y termina en vertederoso tirado al aire libre. A través de la lluvia, el plástico puede llegar a ríos y mares, empeorando la contaminación hídrica.')

@bot.command() 
async def tres(ctx): 
    await ctx.send(f'Estas son algunas de las maneras en las que el plástico llega a afectarnos:') 
    await ctx.send(f'1. Al comer pescado, sal, agua embotellada o incluso respirar, estamos consumiendo microplásticos. Aún se está estudiando el efecto exacto, pero ya se sospecha que pueden causar inflamación y estrés celular. Además, algunos plásticos liberan substancias tóxicas que pueden afectar al sistema hormonal, al cerebro o incluso estar relacionada con ciertos tipos de cancer.') 
    await ctx.send(f'2. El uso de plásticos para calentar comida o almacenar alimentos puede liberar químicos nocivos, especialmente si el plástico no es apto para altas temperaturas. ')
    await ctx.send(f'3. Vivir en lugares llenos de basura plástica no solo es desagradable, también aumenta el riesgo de enfermedades y afecta la calidad de vida.') 
    await ctx.send(f'4. Las playas y ríos contaminados con plástico pueden ahuyentar turistas y afectar a comunidades que dependen de esas actividades.')

@bot.command() 
async def clasificar(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre = archivo.filename
            url = archivo.url
            await archivo.save(nombre)
            await ctx.send("Archivo guardado en {nombre}")
            class_name = get_class("keras_model.h5", "labels.txt", nombre)

            try:

                if class_name == "Queques":
                    await ctx.send("Esto es un queue! Así es como puedes hacer diferentes tipos:")
                    await ctx.send("""🍰 **Queque de Vainilla**

    **Ingredientes:**
    - 2 tazas de harina
    - 1 taza de azúcar
    - 1/2 taza de mantequilla (a temperatura ambiente)
    - 3 huevos
    - 1 taza de leche
    - 2 cucharaditas de polvo de hornear
    - 1 cucharadita de esencia de vainilla
    - 1 pizca de sal

    **Preparación:**
    1. Precalentar el horno a 180 °C y engrasar un molde.
    2. Batir la mantequilla con el azúcar hasta que esté cremosa.
    3. Agregar los huevos uno a uno y luego la esencia de vainilla.
    4. Incorporar la harina, polvo de hornear y sal, alternando con la leche.
    5. Verter la mezcla en el molde y hornear 35-40 minutos, hasta que el palillo salga limpio.
    """)
                
                    await ctx.send("""🍫 **Queque de Chocolate**

    **Ingredientes:**
    - 1 3/4 tazas de harina
    - 3/4 taza de cacao en polvo sin azúcar
    - 1 1/2 tazas de azúcar
    - 1/2 taza de mantequilla
    - 2 huevos
    - 1 taza de leche
    - 1/2 taza de agua caliente
    - 2 cucharaditas de polvo de hornear
    - 1 cucharadita de esencia de vainilla
    - 1 pizca de sal

    **Preparación:**
    1. Precalentar el horno a 180 °C y engrasar un molde.
    2. Batir mantequilla con azúcar hasta que esté esponjosa.
    3. Agregar huevos y vainilla, batiendo bien.
    4. Añadir harina, cacao, polvo de hornear y sal, alternando con la leche.
    5. Incorporar el agua caliente lentamente.
    6. Verter la mezcla en el molde y hornear 40-45 minutos, hasta que el palillo salga seco.
    """)
                
                    await ctx.send("""❤️ **Queque Red Velvet**

    **Ingredientes:**
    - 2 1/2 tazas de harina
     1 taza de azúcar
    - 1/2 taza de mantequilla
    - 2 huevos
     1 taza de buttermilk (leche con 1 cda de vinagre o limón)
    - 2 cdas de cacao en polvo
    - 1 cdta de bicarbonato
    - 1 cdta de vinagre blanco
    - 2 cdtas de esencia de vainilla
    - Colorante rojo al gusto
    - 1 pizca de sal

    **Preparación:**
    1. Precalentar el horno a 175 °C y engrasar un molde.
    2. Batir mantequilla con azúcar, añadir huevos y vainilla.
    3. Mezclar harina, cacao y sal, e incorporar alternando con el buttermilk.
    4. Añadir el colorante rojo y mezclar bien.
    5. Disolver bicarbonato en vinagre e incorporarlo.
    6. Verter en el molde y hornear 40 minutos. Dejar enfriar antes de desmoldar.
    """)


                elif class_name == "Brownies":
                    await ctx.send("esto es un Brownie!! Aquí tienes como hacer uno:")

                    await ctx.send("""🍫 **Brownies Caseros**

    **Ingredientes:**
    - 1 taza de mantequilla derretida
    - 2 tazas de azúcar
    - 4 huevos
    - 1 taza de harina
    - 1 taza de cacao en polvo sin azúcar
    - 1 cdta de esencia de vainilla
    - 1/2 cdta de sal
    - 1/2 cdta de polvo de hornear
    - (Opcional) 1 taza de nueces o chispas de chocolate

    **Preparación:**
    1. Precalentar el horno a 180 °C y engrasar un molde cuadrado.
    2. Mezclar la mantequilla derretida con el azúcar y la vainilla.
    3. Agregar los huevos uno a uno, batiendo después de cada adición.
    4. Incorporar la harina, cacao, sal y polvo de hornear, mezclando suavemente.
    5. (Opcional) Añadir nueces o chispas de chocolate.
    6. Verter la mezcla en el molde y hornear 30-35 minutos.  
    7. Dejar enfriar antes de cortar en cuadros y disfrutar.
    """)

                elif class_name == "Cup cakes":
                    await ctx.send("Esto es un cup cake!! Aquí tienes como hacer diferentes tipos:")

                    await ctx.send("""🧁 **Cupcakes de Vainilla**

    **Ingredientes:**
    - 1 1/2 tazas de harina
    - 1 taza de azúcar
    - 1/2 taza de mantequilla (a temperatura ambiente)
    - 2 huevos
    - 1/2 taza de leche
    - 1 1/2 cdta de polvo de hornear
    - 1 cdta de esencia de vainilla
    - 1 pizca de sal

    **Preparación:**
    1. Precalentar el horno a 180 °C y preparar una bandeja con capacillos.
    2. Batir la mantequilla con el azúcar hasta que esté cremosa.
    3. Agregar los huevos uno a uno y luego la esencia de vainilla.
    4. Incorporar la harina, polvo de hornear y sal, alternando con la leche.
    5. Repartir la mezcla en los capacillos (3/4 de su capacidad).
    6. Hornear 18-20 minutos, hasta que un palillo salga limpio.
    7. Dejar enfriar antes de decorar.
    """)

                    await ctx.send("""🧁🍫 **Cupcakes de Chocolate**

    **Ingredientes:**
    - 1 taza de harina
    - 1/2 taza de cacao en polvo sin azúcar
    - 1 taza de azúcar
    - 1/2 taza de mantequilla
    - 2 huevos
    - 1/2 taza de leche
    - 1 cdta de esencia de vainilla
    - 1 cdta de polvo de hornear
    - 1 pizca de sal

    **Preparación:**
    1. Precalentar el horno a 180 °C y colocar capacillos en una bandeja de cupcakes.
    2. Batir mantequilla con azúcar hasta que esté esponjosa.
    3. Agregar los huevos y la vainilla, mezclando bien.
    4. Incorporar la harina, cacao, polvo de hornear y sal, alternando con la leche.
    5. Repartir la mezcla en los capacillos (3/4 de su capacidad).
    6. Hornear 18-22 minutos, hasta que al insertar un palillo salga seco.
    7. Dejar enfriar antes de decorar o glasear.
    """)


                elif class_name == "Macarons":

                    await ctx.send("""💚 **Macarons de Pistacho**

**Ingredientes:**
- 1 taza de harina de almendra
- 1 taza de azúcar en polvo
- 3 claras de huevo
- 1/2 taza de azúcar
- Colorante verde
- 1/2 taza de crema de pistacho o buttercream de pistacho

**Preparación:**
1. Tamizar la harina de almendra con el azúcar en polvo.
2. Batir claras a punto de nieve, añadir azúcar poco a poco hasta merengue firme.
3. Incorporar el colorante y la mezcla seca con movimientos envolventes.
4. Formar círculos en bandeja con papel encerado y dejar reposar 30 min.
5. Hornear a 150 °C por 15 min.
6. Rellenar con crema o buttercream de pistacho y unir las tapas.
""")
                    
                    await ctx.send("""🤎 **Macarons de Chocolate**

**Ingredientes:**
- 1 taza de harina de almendra
- 3/4 taza de azúcar en polvo
- 1/4 taza de cacao en polvo
- 3 claras de huevo
- 1/2 taza de azúcar
- 1/2 taza de ganache de chocolate (para el relleno)

**Preparación:**
1. Tamizar harina de almendra, azúcar en polvo y cacao.
2. Batir claras a punto de nieve, añadir azúcar poco a poco hasta merengue firme.
3. Incorporar la mezcla seca con movimientos envolventes.
4. Formar círculos en bandeja con papel encerado y dejar reposar 30 min.
5. Hornear a 150 °C por 15 min.
6. Rellenar con ganache de chocolate y unir las tapas.
""")

                    await ctx.send("""🍓 **Macarons de Fresa**

**Ingredientes:**
- 1 taza de harina de almendra
- 1 taza de azúcar en polvo
- 3 claras de huevo
- 1/2 taza de azúcar
- Colorante rosado
- 1/2 taza de buttercream o mermelada de fresa (para el relleno)

**Preparación:**
1. Tamizar harina de almendra con azúcar en polvo.
2. Batir claras a punto de nieve, añadir azúcar poco a poco hasta merengue firme.
3. Incorporar el colorante y la mezcla seca con movimientos envolventes.
4. Formar círculos en bandeja con papel encerado y dejar reposar 30 min.
5. Hornear a 150 °C por 15 min.
6. Rellenar con buttercream o mermelada de fresa y unir las tapas.
""")

                elif class_name == "Galletas":
                    await ctx.send("""🍪 **Galletas con Chispas de Chocolate**

**Ingredientes:**
- 2 1/4 tazas de harina
- 1 taza de mantequilla (a temperatura ambiente)
- 3/4 taza de azúcar blanca
- 3/4 taza de azúcar moreno
- 2 huevos
- 2 cdta de esencia de vainilla
- 1 cdta de bicarbonato de sodio
- 1/2 cdta de sal
- 2 tazas de chispas de chocolate

**Preparación:**
1. Precalentar el horno a 180 °C y preparar una bandeja con papel encerado.
2. Batir la mantequilla con los dos tipos de azúcar hasta que esté cremosa.
3. Agregar los huevos uno a uno, luego la vainilla.
4. Añadir la harina, el bicarbonato y la sal, mezclando bien.
5. Incorporar las chispas de chocolate.
6. Formar bolitas de masa y colocarlas separadas en la bandeja.
7. Hornear de 10 a 12 minutos hasta que estén doradas en los bordes.
8. Dejar enfriar unos minutos antes de moverlas.
""")

            except:
                await ctx.send("Ha ocurrido un error, no se ha podido clasificar, por favor, envíe una imagen en el formato correcto.")        

    else:
        await ctx.send("No hay archivos adjuntos en el mensaje...")

bot.run("token")