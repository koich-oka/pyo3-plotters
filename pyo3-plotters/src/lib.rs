use pyo3::prelude::*;

mod plot;
use plot::plot;

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn plot_with_plotters(out_file_name: String, start: f32, end: f32) -> PyResult<()> {
    plot(out_file_name, start, end);
    Ok(())
}

#[pymodule]
fn pyo3_plotters(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(plot_with_plotters, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
