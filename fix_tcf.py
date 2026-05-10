import json, random, os

PATH = "app/src/main/assets/questions/"

questions = [
    ("What are natural fibres?", "Fibres obtained from plants and animals"),
    ("Which of the following is a natural fibre?", "Cotton"),
    ("What is a synthetic fibre?", "A fibre made from chemicals"),
    ("Which fibre comes from the flax plant?", "Linen"),
    ("What animal produces silk?", "Silkworm"),
    ("Which synthetic fibre is known for its strength and elasticity?", "Nylon"),
    ("What is the process of making yarn from fibres called?", "Spinning"),
    ("Which fabric is most absorbent?", "Cotton"),
    ("What does GSM stand for in fabric?", "Grams per square metre"),
    ("Which weave produces a diagonal pattern?", "Twill weave"),
    ("What is the selvedge of a fabric?", "The finished edge that prevents fraying"),
    ("Which fabric construction method uses loops?", "Knitting"),
    ("What is warp in weaving?", "Threads running lengthwise on the loom"),
    ("What is weft in weaving?", "Threads running crosswise on the loom"),
    ("Which fabric is produced by matting fibres together?", "Felt"),
    ("What is a blended fabric?", "A fabric made from two or more different fibres"),
    ("Which fibre is known for being lightweight and quick-drying?", "Polyester"),
    ("What is the grain of a fabric?", "The direction of the threads in the fabric"),
    ("Which tool is used to measure fabric?", "Measuring tape"),
    ("What is a pattern in sewing?", "A template used to cut fabric pieces"),
    ("Which stitch is used to join two pieces of fabric?", "Seam"),
    ("What is a hem?", "A folded and stitched edge of fabric"),
    ("Which sewing machine foot is used for zippers?", "Zipper foot"),
    ("What does ease mean in a sewing pattern?", "Extra room added for comfort and movement"),
    ("What is the purpose of interfacing?", "To add structure and support to fabric"),
    ("Which type of seam is most durable?", "French seam"),
    ("What is a dart in clothing construction?", "A folded tuck to shape fabric to the body"),
    ("Which element of design refers to the outline of a garment?", "Line"),
    ("What are the primary colours?", "Red, yellow and blue"),
    ("Which colour scheme uses colours next to each other on the colour wheel?", "Analogous"),
    ("What is the principle of balance in design?", "Equal distribution of visual weight"),
    ("Which principle of design refers to the repetition of elements?", "Rhythm"),
    ("What does emphasis in design mean?", "Creating a focal point or centre of interest"),
    ("Which fabric care symbol means do not bleach?", "A triangle with a cross"),
    ("What temperature does a hot iron setting reach?", "210 degrees Celsius"),
    ("Which fabric requires dry cleaning only?", "Silk"),
    ("What does the tub symbol on a care label indicate?", "Washing instructions"),
    ("Which fibre shrinks when washed in hot water?", "Wool"),
    ("What is pilling on fabric?", "Small balls of fibre that form on the surface"),
    ("Which fabric is best for hot climates?", "Cotton"),
    ("What is a gore in garment construction?", "A triangular piece of fabric that adds fullness"),
    ("Which type of pleat faces away from the centre?", "Box pleat"),
    ("What is a facing in sewing?", "A piece of fabric used to finish raw edges"),
    ("Which tool is used to transfer pattern markings to fabric?", "Tracing wheel"),
    ("What is the bias of a fabric?", "The diagonal direction at 45 degrees to the grain"),
    ("Which stitch is used for gathering fabric?", "Running stitch"),
    ("What is a seam allowance?", "The extra fabric between the seam line and the cut edge"),
    ("Which fastener uses interlocking teeth?", "Zip/zipper"),
    ("What is applique?", "Decorative fabric pieces sewn onto a base fabric"),
    ("Which fabric is produced from wood pulp?", "Viscose/Rayon"),
    ("What is the purpose of a toile?", "A test garment made in cheap fabric before cutting the final fabric"),
    ("Which fibre is naturally flame resistant?", "Wool"),
    ("What is mercerisation?", "A finishing process that increases the strength and lustre of cotton"),
    ("Which dye is used for natural fibres like cotton?", "Reactive dye"),
    ("What is a motif in textile design?", "A single design unit that can be repeated"),
    ("Which printing method uses a mesh screen?", "Screen printing"),
    ("What is tie-dyeing?", "A method of dyeing fabric by tying sections to resist the dye"),
    ("Which finishing process makes fabric water repellent?", "Waterproofing"),
    ("What is sanforizing?", "A process to prevent shrinkage in cotton fabric"),
    ("Which type of fabric has a raised cut pile?", "Velvet"),
    ("What is the purpose of a tailor's ham?", "To press curved seams and shaped areas"),
    ("Which stitch creates a decorative zigzag effect?", "Blanket stitch"),
    ("What is smocking?", "A decorative technique that gathers fabric in a pattern"),
    ("Which era introduced the hoopskirt?", "Victorian era"),
    ("What is haute couture?", "High-end custom-fitted fashion made by leading designers"),
    ("Which designer created the little black dress?", "Coco Chanel"),
    ("What is ready-to-wear clothing?", "Mass-produced clothing in standard sizes"),
    ("Which fabric characteristic refers to how it drapes?", "Hand or drape"),
    ("What is the warp knit used for?", "Swimwear and lingerie"),
    ("Which sewing technique prevents raw edges from fraying?", "Overcasting or serging"),
    ("What is the purpose of stay stitching?", "To prevent curved edges from stretching"),
    ("Which tool measures seam allowances accurately?", "Seam gauge"),
    ("What is a raglan sleeve?", "A sleeve that extends to the collar without a shoulder seam"),
    ("Which fastener is sewn and requires a buttonhole?", "Button"),
    ("What does the term bias cut mean in fashion?", "Cutting fabric diagonally across the grain"),
    ("Which fibre absorbs moisture and wicks it away?", "Bamboo"),
    ("What is a flat-felled seam used for?", "Strong visible seams in jeans and sportswear"),
    ("Which element of design refers to surface decoration?", "Texture"),
    ("What is a mood board in fashion design?", "A visual collage that communicates design concepts"),
    ("Which country is known for producing fine wool?", "Australia"),
    ("What is sustainable fashion?", "Clothing produced with minimal environmental and social impact"),
    ("Which fabric is created by bonding fibres with heat?", "Non-woven fabric"),
    ("What is a capsule wardrobe?", "A small collection of versatile, timeless clothing"),
    ("Which stitch is used for hand sewing buttons?", "Thread shank stitch"),
    ("What does RTW stand for in fashion?", "Ready to wear"),
    ("Which tool is used to open seams when pressing?", "Seam roll"),
    ("What is batik?", "A wax-resist dyeing technique applied to cloth"),
    ("Which fabric weave produces a checkerboard pattern?", "Plain weave"),
    ("What is yarn count?", "A measure of the fineness or thickness of yarn"),
    ("Which finishing process adds sheen to fabric?", "Calendering"),
    ("What is a princess seam?", "A vertical seam from shoulder to hem that shapes the bodice"),
    ("Which fabric is made from the hair of the Angora goat?", "Mohair"),
    ("What is negative ease in a garment?", "When the garment is smaller than the body measurement"),
    ("Which stitch is used for attaching elastic?", "Zigzag stitch"),
    ("What is a placket?", "An opening in a garment that allows it to be put on and taken off"),
    ("Which tool is used to press open seams?", "Iron and pressing cloth"),
    ("What is a trade mark in the fashion industry?", "A symbol or name that identifies a brand"),
    ("Which type of collar lies flat against the garment?", "Peter Pan collar"),
    ("What is grading a pattern?", "Adjusting a pattern to a different size"),
]

random.shuffle(questions)

all_wrong = [q[1] for q in questions]

for lvl in range(1, 21):
    data = []
    pool = questions.copy()
    random.shuffle(pool)
    selected = pool[:20]
    for q, a in selected:
        wrong = [x for x in all_wrong if x != a]
        random.shuffle(wrong)
        opts = [a] + wrong[:3]
        random.shuffle(opts)
        ci = opts.index(a)
        data.append({"question": q, "options": opts, "correctIndex": ci})
    out = f"{PATH}cxc_tcf_l{lvl}.json"
    with open(out, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ cxc_tcf_l{lvl}.json ({len(data)} questions)")

print("\nDone!")
