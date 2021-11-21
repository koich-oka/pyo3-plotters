use plotters::coord::Shift;
use plotters::data::fitting_range;
use plotters::prelude::*;
use std::slice::Iter;

pub fn plot(out_file_name: String, x: Vec<f32>) -> Result<(), Box<dyn std::error::Error>> {
    let root_area = BitMapBackend::new(&out_file_name, (1024, 768)).into_drawing_area();

    root_area.fill(&WHITE)?;

    let root_area = root_area.titled("Image Title", ("sans-serif", 60))?;
    let (upper, lower) = root_area.split_vertically(384);
    let x_iter = x.iter();

    let mut cc1 = ChartBuilder::on(&upper)
        .margin(5)
        .set_all_label_area_size(50)
        .build_cartesian_2d(fitting_range(x_iter.to_owned()), -1.2f32..1.2f32)?;

    cc1.configure_mesh()
        .x_labels(20)
        .y_labels(10)
        .disable_mesh()
        .x_label_formatter(&|v| format!("{:.1}", v))
        .y_label_formatter(&|v| format!("{:.1}", v))
        .draw()?;

    cc1.draw_series(LineSeries::new(
        x_iter.to_owned().map(|&x| (x, x.sin())),
        RED.stroke_width(1),
    ))?
    .label("Sine")
    .legend(|(x, y)| PathElement::new(vec![(x, y), (x + 20, y)], &RED));

    cc1.configure_series_labels().border_style(&BLACK).draw()?;

    let mut cc2 = ChartBuilder::on(&lower)
        .margin(5)
        .set_all_label_area_size(50)
        .build_cartesian_2d(fitting_range(x_iter.to_owned()), -1.2f32..1.2f32)?;

    cc2.configure_mesh()
        .x_labels(20)
        .y_labels(10)
        .disable_mesh()
        .x_label_formatter(&|v| format!("{:.1}", v))
        .y_label_formatter(&|v| format!("{:.1}", v))
        .draw()?;

    cc2.draw_series(LineSeries::new(
        x_iter.to_owned().map(|&x| (x, x.sin())),
        RED.stroke_width(1),
    ))?
    .label("Sine")
    .legend(|(x, y)| PathElement::new(vec![(x, y), (x + 20, y)], &RED));

    cc2.configure_series_labels().border_style(&BLACK).draw()?;

    // To avoid the IO failure being ignored silently, we manually call the present function
    root_area.present().expect("Unable to write result to file, please make sure 'plotters-doc-data' dir exists under current dir");
    println!("Result has been saved to {}", &out_file_name);
    Ok(())
}
